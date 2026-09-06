import os
import json
import google.generativeai as genai


print("🧠 AI Carousel Agent Started")


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-3.6-flash"
)


with open(
    "output/research_result.json"
) as f:
    trend = json.load(f)


with open(
    "output/creative_plan.json"
) as f:
    brand = json.load(f)


prompt = f"""
Kamu adalah AI Content Director Bos Sony Creative Studio.

Brand:
{brand}

Trend:
{trend}


Buat Instagram carousel 6 slide.

Output HARUS JSON:

{{
"title":"",
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

Jangan beri penjelasan.
Hanya JSON.
"""


response = model.generate_content(
    prompt
)


content = response.text


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
        indent=2
    )


print(
    "✅ AI Carousel Generated"
)
