from google import genai
import json, os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def screen_candidate(input_text: str) -> dict:
    mock_response = {
        "score": 8,
        "skills_match": ["Python", "NLP", "Scikit-learn"],
        "recommendation": "shortlist",
        "reason": "Strong Python and NLP skills match the requirements."
    }
    print(f"[MOCK] Screening: {input_text}")
    return mock_response
