import os
import json
from openai import OpenAI


print("🖼 Image Generator Started")


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


with open(
    "output/image_prompts.json"
) as f:
    prompts = json.load(f)


os.makedirs(
    "assets/generated",
    exist_ok=True
)


for item in prompts:

    response = client.images.generate(

        model="gpt-image-1",

        prompt=item["prompt"] 
        + 
        ", premium editorial advertising style, "
        "creative studio photography, "
        "vertical 4:5",

        size="1024x1536"

    )


    image_url = response.data[0].url


    print(
        "Generated slide:",
        item["slide"]
    )


    # sementara simpan URL dulu
    # download layer ditambah berikutnya


    with open(
        f"assets/generated/slide_{item['slide']:02}.txt",
        "w"
    ) as f:

        f.write(image_url)


print(
    "✅ Image generation completed"
)
