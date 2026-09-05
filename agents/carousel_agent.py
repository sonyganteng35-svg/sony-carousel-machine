import json
import os


print("🎨 Carousel Agent Started")


os.makedirs("output", exist_ok=True)


strategy = {
    "title": "AI editing workflow untuk creator",
    "platform": "Instagram Carousel",
    "slides": [
        {
            "slide":1,
            "headline":"AI bukan menggantikan editor",
            "purpose":"Hook"
        },
        {
            "slide":2,
            "headline":"Masalah creator: edit lama, ide habis",
            "purpose":"Problem"
        },
        {
            "slide":3,
            "headline":"AI membantu proses repetitif",
            "purpose":"Insight"
        },
        {
            "slide":4,
            "headline":"Gunakan AI sebagai assistant editor",
            "purpose":"Solution"
        },
        {
            "slide":5,
            "headline":"Follow Bos Sony Creative Studio",
            "purpose":"CTA"
        }
    ]
}


with open(
    "output/04_visual_direction.json",
    "w"
) as f:
    json.dump(strategy,f,indent=2)


with open(
    "output/FINAL_CAROUSEL.json",
    "w"
) as f:
    json.dump(strategy,f,indent=2)


print("✅ Carousel generated")
