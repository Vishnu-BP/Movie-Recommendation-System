<div align="center">
    <h1>🎬 Gemini RAG Movie Recommender Engine</h1>
    <p>Personalized film suggestions powered by Google's Gemini Model with Google Search Grounding.</p>
    
    <p>
        <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python 3.10+">
        <img src="https://img.shields.io/badge/FastAPI-0.119.0-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
        <img src="https://img.shields.io/badge/Gemini_API-Flash-1A73E8?style=for-the-badge&logo=google" alt="Gemini API">
        <img src="https://img.shields.io/badge/Firebase-Auth-FFCA28?style=for-the-badge&logo=firebase" alt="Firebase Auth">
        <img src="https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss" alt="Tailwind CSS">
    </p>

</div>

---

## 🌟 1. Introduction

The **Gemini RAG Movie Recommender** is a modern, full-stack web application designed to provide highly relevant and *verifiable* film suggestions. Unlike traditional recommenders based solely on collaborative filtering, this system leverages a powerful Large Language Model (LLM)—**Gemini 2.5 Flash**—augmented with the **Retrieval-Augmented Generation (RAG)** technique.

The user provides criteria (Genre, Mood, Era), and the system performs a real-time grounded search to find current, high-quality matches, complete with movie ratings and plot justifications.

### Key Architectural Highlights

* **Security:** The API key is securely managed on a backend proxy (FastAPI).
* **Grounding:** Utilizes Google Search as an external knowledge source to ensure factual accuracy and currency of movie data.
* **Structured Output:** Employs advanced prompt engineering and JSON parsing to enforce a strict output structure from the LLM.

---

## 💡 2. The RAG Approach (How it Works)

This project's intelligence is defined by the RAG architecture, ensuring quality and verifiability.

### Retrieval (R)
The Gemini model is instructed to use the **Google Search tool** *before* generating a response. When you request a movie, the model performs a real-time, targeted search (e.g., "best Sci-Fi movies from 90s IMDb rating") to retrieve factual data (ratings, plot summaries, release years).

### Generation (G)
The model then uses the retrieved, up-to-date data to formulate three movie recommendations. The system prompt forces the model to:
1.  **Strictly adhere to a JSON schema** for reliable data parsing.
2.  Provide a concise **justification** that explicitly links the recommended movie back to the user's input criteria.

By relying on external, real-time data, the recommender minimizes hallucinations and provides highly personalized, grounded suggestions.

---

## 💻 3. Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend / API** | **Python 3.10+** | Core development language. |
| **Web Framework** | **FastAPI** | High-performance, asynchronous web framework for the API proxy. |
| **AI/ML Engine** | **Google Gemini API (Flash)** | The core model used for RAG and personalized generation. |
| **Secrets Management** | **`python-dotenv`** | Securely loads environment variables (`GEMINI_API_KEY`) locally. |
| **Frontend** | **HTML5, Vanilla JS** | Structure and client-side logic (form handling, API calls). |
| **Styling** | **Tailwind CSS** | Utility-first framework for the clean, dark-themed UI. |
| **Auth (Optional)** | **Firebase Client SDK** | Used for user session management (mocked for local testing). |

---

## 🖼️ 4. Interface Preview

### A. Home Page (Criteria Input)

This is the initial view where the user authenticates (or enters mock mode) and defines their desired film criteria. The inputs drive the specificity of the RAG search.

<div align="center">
    <img src="" alt="Home Page: Movie Criteria Form" style="max-width: 600px; border: 1px solid #30363d; border-radius: 8px;">
    <p>The form captures user preferences for Genre, Mood, and Era.</p>
</div>

### B. Results Page (RAG Output Highlight)

After processing the request, the application displays three highly-ranked suggestions. This view highlights the success of the RAG approach by showing detailed, verifiable movie data and the grounding sources used by the model.

<div align="center">
    <img src="" alt="Results Page: Recommendations with Justifications" style="max-width: 600px; border: 1px solid #30363d; border-radius: 8px;">
    <p>Each recommendation includes a unique justification and links to the web sources used for grounding.</p>
</div>

---

## ⚙️ 5. Local Setup and Installation

Follow these steps to get a local copy of the project running.

### 5.1. Prerequisites
* Python 3.10+
* A **Gemini API Key** (Obtained from Google AI Studio).
* A **Firebase Web App Config** (for optional authentication/user state).

### 5.2. Installation

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL] movieRecomendationSystem
    cd movieRecomendationSystem
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate.bat   # Windows Command Prompt
    # source venv/bin/activate    # macOS/Linux/Git Bash
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r api/requirements.txt
    ```

### 5.3. Configuration (`.env` file)

1.  Create a file named **`.env`** in the project root (`movieRecomendationSystem/`).
2.  Fill it with your credentials:

    ```env
    # .env
    GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_KEY_HERE
    FIREBASE_CONFIG='{"apiKey": "...", "projectId": "...", "appId": "..."}'
    APP_ID="movie-rag-recommender-v1"
    PORT=8000
    ```

### 5.4. Run the Server

Start the FastAPI backend using Uvicorn. This will also serve the static frontend files.

```bash
(venv) uvicorn api.main:app --reload