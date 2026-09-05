import json
import os


print("🎬 Visual Agent Started")


with open(
    "output/FINAL_CAROUSEL.json",
    "r"
) as f:
    carousel = json.load(f)


visuals = []


for slide in carousel["slides"]:

    prompt = {
        "slide": slide["slide"],
        "headline": slide["headline"],
        "image_prompt": (
            "Premium editorial advertising style, "
            "creative editor workspace, "
            "modern AI creator environment, "
            "dramatic lighting, "
            "clean composition, "
            "black white orange color palette, "
            "vertical Instagram carousel 4:5"
        )
    }

    visuals.append(prompt)


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/visual_prompts.json",
    "w"
) as f:
    json.dump(
        visuals,
        f,
        indent=2
    )


print("✅ Visual prompts generated")
