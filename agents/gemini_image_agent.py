import os
import json
import requests
import google.generativeai as genai


print("🖼 Gemini Image Generator Started")


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


with open(
    "output/image_prompts.json"
) as f:
    prompts = json.load(f)


os.makedirs(
    "output/slides",
    exist_ok=True
)


model = genai.GenerativeModel(
    "gemini-2.0-flash-exp"
)


for item in prompts:

    slide = item["slide"]

    prompt = f"""

Create a premium Instagram carousel visual.

Brand:
Bos Sony Creative Studio

Style:
Creative Editor Culture,
Premium Editorial Magazine,
Modern Advertising Agency,
AI Creative Studio.

Format:
Vertical 4:5
1080x1350

Rules:
- no text
- no watermark
- no logo
- realistic professional photography
- cinematic lighting
- premium creator workspace

Visual:
{item["prompt"]}

"""


    print(
        f"Generating slide {slide}"
    )


    response = model.generate_content(
        prompt
    )


    # save response
    output = response.text


    with open(
        f"output/slides/slide_{slide}.txt",
        "w"
    ) as f:

        f.write(output)



print(
"✅ Gemini Image Generation Finished"
)
