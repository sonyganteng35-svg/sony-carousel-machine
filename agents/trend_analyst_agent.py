import json
import os


print("📊 Trend Analyst Agent Started")


with open(
    "output/trend_research.json"
) as f:
    trends = json.load(f)


analysis = []


for item in trends["trends"]:

    score = 0


    # audience relevance

    if item["platform"] in [
        "TikTok",
        "Instagram",
        "CapCut"
    ]:
        score += 3


    # business opportunity

    if "creator" in item["content_angle"].lower():
        score += 2


    # education value

    score += 3


    analysis.append({

        "topic":
        item["keyword"],

        "platform":
        item["platform"],

        "opportunity_score":
        score,

        "recommended_angle":
        (
        "Buat carousel edukasi "
        "dengan problem → solusi → CTA"
        )

    })


result = {

    "top_opportunities":
    sorted(
        analysis,
        key=lambda x:x["opportunity_score"],
        reverse=True
    )

}


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/trend_analysis.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )


print("✅ Trend analysis complete")
