from google import genai
import json, os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def screen_candidate(input_text: str) -> dict:
    prompt = f"""
    Analyze this candidate profile and return ONLY a JSON object with:
    - score (int 1-10)
    - skills_match (list of matched skills)
    - recommendation (string: shortlist/reject/review)
    - reason (string, one sentence)

    Profile: {input_text}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)
