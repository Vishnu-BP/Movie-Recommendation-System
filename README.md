<div align="center">
    <h1>🎬 Dynamic, Grounded Movie Recommendation Engine</h1>
    <p>Personalized film suggestions powered by Google's Gemini Model with Google Search Grounding (RAG).</p>
    
    <p>
        <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python 3.10+">
        <img src="https://img.shields.io/badge/FastAPI-0.119.0-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
        <img src="https://img-shields.io/badge/Gemini_API-Flash-1A73E8?style=for-the-badge&logo=google" alt="Gemini API">
        <img src="https://img.shields.io/badge/Firebase-Auth-FFCA28?style=for-the-badge&logo=firebase" alt="Firebase Auth">
        <img src="https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss" alt="Tailwind CSS">
    </p>

    <p>
        <a href="./frontend/images/Home.png" target="_blank">View Live Home Page Preview</a> | 
        <a href="./frontend/images/Result sheet.png" target="_blank">View Live Results Page Preview</a>
    </p>
</div>

---

## 🌟 1. Introduction

The **Dynamic, Grounded Movie Recommendation Engine** is a modern, full-stack web application designed to provide highly relevant and *verifiable* film suggestions. Unlike traditional systems, this engine leverages a powerful Large Language Model (LLM)—**Gemini 2.5 Flash**—augmented with **Retrieval-Augmented Generation (RAG)**.

The user provides criteria (Genre, Mood, Era), and the system performs a real-time grounded search to find current, high-quality matches, complete with movie ratings and plot justifications.

### Key Architectural Highlights

* **Grounded Decisions:** Minimizes hallucinations by using Google Search for factual grounding (RAG).
* **Security:** The Gemini API key is securely managed on a backend proxy (FastAPI).
* **Structured Output:** Advanced prompt engineering ensures reliable, parseable JSON output from the LLM.

---

## 💡 2. The RAG Approach (How it Works)

The intelligence of this project is defined by its **Dynamic, Grounded** RAG workflow:

### Retrieval (R)
The **Gemini model** is explicitly instructed to use the **Google Search tool** before generating a response. When a user inputs criteria, the model executes a real-time, fact-checking query (e.g., "IMDb ratings for Action Sci-Fi 90s movies") to retrieve up-to-date metadata, thereby making the recommendation *Grounded*.

### Generation (G)
The model uses the retrieved, up-to-date external data to formulate exactly three unique movie recommendations. It is strictly constrained by the system prompt to:
1.  Adhere to a **JSON schema** for clean data transfer.
2.  Provide a concise **justification** that explicitly links the recommended movie back to the user's input criteria.

---

## 💻 3. Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend / API** | **Python 3.10+** | Core development language for the server logic. |
| **Web Framework** | **FastAPI** | High-performance, asynchronous web framework for the secure API proxy. |
| **AI/ML Engine** | **Google Gemini API** | Core model used for RAG and personalized content generation. |
| **Secrets Management** | **`python-dotenv`** | Securely loads environment variables (`GEMINI_API_KEY`) locally. |
| **Frontend** | **HTML5, Vanilla JS** | Structure and client-side logic for dynamic form handling. |
| **Styling** | **Tailwind CSS** | Utility-first framework for the responsive, dark-themed UI. |

---

## 🖼️ 4. Interface Preview

### A. Home Page (Criteria Input)

<div align="center">
    <a href="./frontend/images/Home.png" target="_blank">
        <img src="" alt="Home Page: Movie Criteria Form" style="max-width: 600px; border: 1px solid #30363d; border-radius: 8px;">
    </a>
    <p>The form captures user preferences for Genre, Mood, and Era, initiating the Dynamic RAG search.</p>
</div>

### B. Results Page (Grounded Output)

<div align="center">
    <a href="./frontend/images/Result sheet.png" target="_blank">
        <img src="" alt="Results Page: Recommendations with Justifications" style="max-width: 600px; border: 1px solid #30363d; border-radius: 8px;">
    </a>
    <p>Displays the 3 top recommendations, complete with factual ratings and justifications based on retrieved data.</p>
</div>

---

## ⚙️ 5. Local Setup and Installation

Follow these steps to get a local copy of the project running.

### 5.1. Prerequisites
* Python 3.10+
* A **Gemini API Key** (for backend access).
* A **Firebase Web App Config** (for optional frontend auth).

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

1.  Create a file named **`.env`** in the project root.
2.  Fill it with your credentials (ensure `GEMINI_API_KEY` is unquoted):

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