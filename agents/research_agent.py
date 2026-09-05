import json
from datetime import datetime

brand = json.load(open("config/brand.json"))

research = {
    "date": str(datetime.now()),
    "brand": brand["brand"],
    "topics": [
        {
            "platform": "TikTok",
            "topic": "AI editing workflow",
            "reason": "Creator mencari cara edit lebih cepat"
        },
        {
            "platform": "Instagram",
            "topic": "Carousel edukasi UMKM",
            "reason": "Konten saveable meningkatkan authority"
        },
        {
            "platform": "CapCut",
            "topic": "Template editing HP",
            "reason": "Pemula ingin hasil profesional"
        }
    ]
}

with open("output/research_result.json", "w") as f:
    json.dump(research, f, indent=2)

print("Research agent finished")
