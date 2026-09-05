import json
import os


print("🧠 Decision Agent Started")


with open(
    "output/quality_report.json"
) as f:
    quality = json.load(f)


score = quality.get(
    "total_score",
    0
)


decision = {
    "score": score,
    "action": "",
    "status": ""
}


if score >= 8:

    decision["action"] = "publish"
    decision["status"] = "approved"

else:

    decision["action"] = "revise"
    decision["status"] = "needs_improvement"



os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/decision.json",
    "w"
) as f:

    json.dump(
        decision,
        f,
        indent=2
    )


print(
    "Decision:",
    decision["action"]
)
