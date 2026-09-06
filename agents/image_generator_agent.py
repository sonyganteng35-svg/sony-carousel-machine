import os
import json
import base64
from google import genai
from google.genai import types


print("🖼️ Gemini Image Generator Agent Started")


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


with open(
    "output/visual_prompts.json"
) as f:
    data = json.load(f)


os.makedirs(
    "output/slides",
    exist_ok=True
)


for slide in data["slides"]:

    number = slide["slide"]

    prompt = slide.get(
        "image_prompt",
        slide.get("visual_prompt", "")
    )


    print(
        f"Generating slide {number}"
    )


    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[
            f"""
Create premium Instagram carousel visual.

Brand:
Bos Sony Creative Studio

Style:
Creative Editor Culture,
Premium Editorial,
Modern Advertising.

Format:
- Instagram carousel 4:5
- 1080x1350
- realistic professional photography
- premium creative studio aesthetic

Rules:
- no text
- no watermark
- no random logo

Visual concept:

{prompt}
"""
        ],
        config=types.GenerateContentConfig(
            response_modalities=[
                "IMAGE"
            ]
        )
    )


    image_saved = False


    for part in response.candidates[0].content.parts:

        if part.inline_data:

            image_bytes = base64.b64decode(
                part.inline_data.data
            )


            with open(
                f"output/slides/slide_{number}.png",
                "wb"
            ) as img:

                img.write(
                    image_bytes
                )


            image_saved = True


    if image_saved:
        print(
            f"✅ Slide {number} saved"
        )
    else:
        print(
            f"❌ Slide {number} failed"
        )


print(
    "✅ Gemini image generation finished"
)
