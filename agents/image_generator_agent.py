import os
import json
import requests
from openai import OpenAI


print("🖼️ Image Generator Agent Started")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


with open(
    "output/visual_prompts.json"
) as f:
    slides = json.load(f)


os.makedirs(
    "output/slides",
    exist_ok=True
)


for slide in slides["slides"]:

    number = slide["slide"]
    prompt = slide["image_prompt"]


    print(
        f"Generating slide {number}"
    )


    response = client.images.generate(
        model="gpt-image-1",
        prompt=f"""
        Create premium Instagram carousel visual.

        Brand:
        Bos Sony Creative Studio

        Style:
        Creative Editor Culture,
        Premium Editorial,
        Modern Advertising.

        Requirements:
        - 1080x1350 Instagram format
        - no text
        - no watermark
        - realistic professional design

        Visual:
        {prompt}
        """,
        size="1024x1536"
    )


    image_url = response.data[0].url


    image = requests.get(
        image_url
    ).content


    with open(
        f"output/slides/slide_{number}.png",
        "wb"
    ) as img:

        img.write(image)


print(
"✅ All slides generated"
)
