import os
import json
from google import genai


print("🎠 Carousel Agent Started")


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


with open(
    "output/research_result.json"
) as f:
    research = json.load(f)


with open(
    "output/creative_plan.json"
) as f:
    brand = json.load(f)


prompt = f"""

You are Bos Sony Creative Studio AI.

Create Instagram carousel content.

Brand:
{brand}

Research:
{research}


Create 6 slide carousel.

Return ONLY valid JSON.

Format:

{{
"title":"",
"slides":[
{{
"slide":1,
"headline":"",
"body":"",
"image_prompt":"",
"layout":""
}}
]
}}

No markdown.
No explanation.
"""


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


content = response.text


# bersihkan markdown jika Gemini kasih ```json

content = content.replace(
    "```json",
    ""
)

content = content.replace(
    "```",
    ""
)


data = json.loads(
    content.strip()
)


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/FINAL_CAROUSEL.json",
    "w"
) as f:

    json.dump(
        data,
        f,
        indent=2,
        ensure_ascii=False
    )


print(
"✅ Carousel generated"
)
