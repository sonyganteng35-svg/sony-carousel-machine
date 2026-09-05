import json
import os


print("🎨 Canva Production Agent Started")


with open(
    "output/FINAL_CAROUSEL.json",
    "r"
) as f:
    carousel = json.load(f)


slides = []


for item in carousel["slides"]:

    slide = {

        "slide_number": item["slide"],

        "canvas": {
            "size": "1080x1350",
            "ratio": "4:5"
        },

        "layout": {
            "style": "premium editorial",
            "grid": "12 column layout",
            "alignment": "asymmetric"
        },

        "brand": {
            "primary_color": "#111111",
            "secondary_color": "#F7F7F5",
            "accent_color": "#F26B38"
        },

        "typography": {
            "headline": "Space Grotesk Bold",
            "body": "Inter Medium"
        },

        "headline": item["headline"],

        "visual_direction":
        "Creative editor workspace, premium advertising photography, modern creator environment",

        "elements": [
            "large slide number",
            "orange accent line",
            "clean whitespace",
            "editorial composition"
        ]
    }


    slides.append(slide)



canva_output = {

    "brand":
    "Bos Sony Creative Studio",

    "format":
    "Instagram Carousel",

    "slides":
    slides

}



os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/canva_brief.json",
    "w"
) as f:

    json.dump(
        canva_output,
        f,
        indent=2
    )


print("✅ Canva brief generated")
