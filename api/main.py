# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from google import genai
import os
import json
from pathlib import Path
import re

# ==========================================================
# 🛑 CRITICAL FIX: Load Environment Variables from .env
from dotenv import load_dotenv
load_dotenv() 
# ==========================================================


# --- 1. SETUP & PATH RESOLUTION ---

# Define the absolute path to the project root and the frontend folder
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Initialize FastAPI app
app = FastAPI(title="Gemini RAG Recommender API")

# Initialize Gemini Client
try:
    # Client will automatically pick up GEMINI_API_KEY from os.environ
    client = genai.Client()
except Exception as e:
    # Keep the print statement for visibility, but set client to None
    print("WARNING: Gemini client failed to initialize. Check GEMINI_API_KEY.")
    client = None 

# --- 2. CORS (Cross-Origin Resource Sharing) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 3. INPUT SCHEMA ---
# Defines the expected data structure from the frontend
class RecommendationRequest(BaseModel):
    genre: str
    mood: str
    era: str

# --- 4. THE RAG ENDPOINT ---
@app.post("/api/recommend")
async def get_recommendations_api(req: RecommendationRequest):
    
    if client is None:
        raise HTTPException(status_code=500, detail="Gemini API service is unavailable. Check server logs.")

    # This is the RAG System Prompt
    system_prompt = """You are a world-class film critic and a Retrieval-Augmented Generation (RAG) system. Your task is to provide 3 highly personalized movie recommendations based on the user's criteria. You must use the Google Search grounding tool to retrieve real and up-to-date movie metadata (IMDb/Wikipedia knowledge) to ensure accuracy.

    The output MUST be a JSON array of objects, strictly adhering to the following schema. Do NOT include any introductory or concluding text outside of the JSON block.
    JSON Schema: [{"title": "Movie Title", "year": "Release Year", "rating": "IMDb or user rating (e.g., 8.5/10)", "justification": "A brief (1-2 sentence) explanation of why this movie perfectly matches the user's criteria, grounded in real movie facts."}]
    """
    
    # This is the User's Query (Augmented with criteria)
    user_query = f"""My preferences are:
    1. Genre: {req.genre}
    2. Mood/Vibe: {req.mood}
    3. Time Period: {req.era}

    Please generate exactly 3 movie recommendations. Use your knowledge and external search to find and verify the best movies, and provide the output strictly in the requested JSON format."""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_query,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[{"google_search": {}}],  # Activates RAG/Grounding
            ),
        )

        # 🛑 FIX APPLIED: Robust JSON Extraction (Removes markdown and excess text)
        raw_text = response.text.strip()
        
        # Find the start and end of the JSON block (looking for array brackets)
        json_start = raw_text.find('[')
        json_end = raw_text.rfind(']')
        
        if json_start != -1 and json_end != -1 and json_end > json_start:
            # Extract the pure JSON list string
            json_string = raw_text[json_start : json_end + 1]
            recommendations = json.loads(json_string)
        else:
            # Fallback for when no clean array structure is found
            print(f"Failed to find JSON block in response: {raw_text[:200]}...")
            raise Exception("Gemini returned unstructured or empty content.")


        # Final return
        return {
            "recommendations": recommendations,
            # 🛑 FIX APPLIED: Removed the problematic .to_dict() call. 
            # FastAPI's encoder will now serialize the object directly, resolving the AttributeError.
            "groundingMetadata": response.candidates[0].grounding_metadata if response.candidates and response.candidates[0].grounding_metadata else None
        }
        
    except Exception as e:
        # Check if the error is due to bad API response/JSON parsing
        error_detail = f"Gemini API or Parsing Error: {e}"
        print(error_detail)
        raise HTTPException(status_code=500, detail=error_detail)

# --- 5. SERVING STATIC FILES (Frontend) ---
# FIX APPLIED: Use the absolute path (FRONTEND_DIR) to ensure the index.html is found.
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")