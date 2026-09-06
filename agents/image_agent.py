import json
import os


print("🖼 Image Prompt Agent Started")


with open(
    "output/FINAL_CAROUSEL.json"
) as f:
    carousel = json.load(f)


prompts = []


for slide in carousel["slides"]:

    prompts.append({

        "slide":
        slide["slide"],

        "prompt":
        slide.get(
            "visual_prompt",
            "premium creative workspace"
        ),

        "style":
        (
        "premium editorial, "
        "modern advertising, "
        "creative editor culture, "
        "vertical 4:5"
        )

    })


with open(
    "output/image_prompts.json",
    "w"
) as f:

    json.dump(
        prompts,
        f,
        indent=2
    )


print(
    "✅ Image prompts created"
)
