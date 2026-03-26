import time
from src.llm_client import screen_candidate

def process_batch(csv_path):
    import pandas as pd
    df = pd.read_csv(csv_path)
    results = []
    for _, row in df.iterrows():
        profile = row.to_string()
        result = screen_candidate(profile)
        results.append(result)
        time.sleep(4)  # stay within free tier rate limits
    return results