import os
import json
from google import genai


print("🧠 AI Carousel Agent Started")


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Load creative plan
with open(
    "output/creative_plan.json",
    "r"
) as f:
    brand = json.load(f)


# Load research result
with open(
    "output/research_result.json",
    "r"
) as f:
    trend = json.load(f)



prompt = f"""
Kamu adalah AI Content Director
Bos Sony Creative Studio.

Brand:
{brand}

Trend Research:
{trend}


Buat Instagram carousel profesional.

Format:
6 slide.

Output HARUS JSON valid saja.

Schema:

{{
"title":"",
"hook":"",
"slides":[
{{
"slide":1,
"headline":"",
"body":"",
"visual_prompt":"",
"layout":""
}}
],
"caption":"",
"cta":""
}}

Jangan gunakan markdown.
Jangan pakai ```json.
Hanya JSON.
"""



response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)



content = response.text


# Bersihkan kemungkinan markdown
content = content.replace(
    "```json",
    ""
)

content = content.replace(
    "```",
    ""
)

content = content.strip()



data = json.loads(
    content
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
    "✅ AI Carousel Generated"
)
