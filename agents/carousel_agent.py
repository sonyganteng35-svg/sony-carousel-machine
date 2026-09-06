import os
import json
from openai import OpenAI


print("🧠 AI Carousel Agent Started")


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
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
]
}}

Jangan beri penjelasan lain.
"""


response = client.chat.completions.create(

    model="gpt-5.6-sol",

    messages=[

        {
        "role":"system",
        "content":
        "You are an expert content strategist."
        },

        {
        "role":"user",
        "content":prompt
        }

    ],

    temperature=0.8

)



content = response.choices[0].message.content


data = json.loads(content)


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
