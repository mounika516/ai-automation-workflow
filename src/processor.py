import pandas as pd
from src.llm_client import screen_candidate

def process_batch(input_file: str) -> list:
    df = pd.read_csv(input_file)
    results = []
    for _, row in df.iterrows():
        profile = f"Name: {row['name']}, Skills: {row['skills']}, Experience: {row['experience']}"
        result = screen_candidate(profile)
        result["name"] = row["name"]
        results.append(result)
    return results
