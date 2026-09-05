import json
import os
from datetime import datetime


print("🔥 Real Trend Research Agent Started")


with open(
    "config/research_sources.json"
) as f:
    sources = json.load(f)


trend_result = {

    "date":
    datetime.now().strftime("%Y-%m-%d"),

    "trends":[]

}


for source in sources["sources"]:

    trend_result["trends"].append({

        "platform":
        source["name"],

        "keyword":
        source["keyword"],

        "content_angle":
        "Buat konten edukasi praktis untuk creator dan UMKM"

    })



os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/trend_research.json",
    "w"
) as f:

    json.dump(
        trend_result,
        f,
        indent=2
    )


print("✅ Trend research completed")
