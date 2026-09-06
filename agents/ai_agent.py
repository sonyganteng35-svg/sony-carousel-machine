import os
import json
import google.generativeai as genai


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

with open(
    "output/creative_plan.json"
) as f:
    creative = json.load(f)


prompt = f"""
Kamu adalah AI Content Director Bos Sony Creative Studio.

Brand:
Bos Sony Creative Studio

Style:
Creative Editor Culture,
Premium Editorial,
Modern Advertising


Buatkan Instagram carousel profesional.

Creative direction:
{creative}


Output wajib JSON:

{{
"title":"",
"hook":"",
"slides":[
{{
"slide":1,
"headline":"",
"body":"",
"visual_direction":""
}}
],
"caption":"",
"cta":""
}}

Jangan beri penjelasan.
Hanya JSON.
"""


response = client.chat.completions.create(

    model="gpt-5-mini",

    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ],

    temperature=0.8
)


content = response.choices[0].message.content


data = json.loads(content)


with open(
    "output/ai_carousel.json",
    "w"
) as f:

    json.dump(
        data,
        f,
        indent=2
    )


print(
"AI generation finished"
)
