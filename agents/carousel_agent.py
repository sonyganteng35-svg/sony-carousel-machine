import os
import json
import google.generativeai as genai


print("🧠 AI Carousel Agent Started")


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


with open(
    "output/research_result.json",
    "r"
) as f:
    trend = json.load(f)


with open(
    "output/creative_plan.json",
    "r"
) as f:
    brand = json.load(f)



prompt = f"""
Kamu adalah AI Content Director
Bos Sony Creative Studio.

Brand:
{brand}

Trend:
{trend}


Buat Instagram carousel profesional.

Buat 6 slide.

Output WAJIB JSON valid:

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

Jangan pakai markdown.
Jangan pakai ```json.
Hanya JSON.
"""



response = model.generate_content(
    prompt
)



content = response.text


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
