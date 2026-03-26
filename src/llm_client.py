import google.generativeai as genai
import json, os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def screen_candidate(input_text: str) -> dict:
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Analyze this candidate profile and return ONLY a JSON object with:
    - score (int 1-10)
    - skills_match (list of matched skills)
    - recommendation (string: shortlist/reject/review)
    - reason (string, one sentence)

    Profile: {input_text}
    """
    response = model.generate_content(prompt)
    return json.loads(response.text)
