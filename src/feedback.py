import json

def evaluate_and_refine(results: list, threshold: int = 6) -> dict:
    shortlisted = [r for r in results if r["score"] >= threshold]
    rejected = [r for r in results if r["score"] < threshold]

    feedback_log = {
        "total_processed": len(results),
        "shortlisted": len(shortlisted),
        "rejected": len(rejected),
        "avg_score": sum(r["score"] for r in results) / len(results),
        "low_confidence": [r["name"] for r in results if r["recommendation"] == "review"]
    }

    with open("data/outputs/feedback_log.json", "w") as f:
        json.dump(feedback_log, f, indent=2)

    return feedback_log
