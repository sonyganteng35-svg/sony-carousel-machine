import os
import json
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


brand = {
    "name": "Bos Sony Creative Studio",
    "positioning": "Membantu UMKM dan creator membuat video HP terlihat seperti iklan profesional",
    "style": [
        "editorial magazine",
        "premium creative studio",
        "modern internet culture"
    ],
    "tone": [
        "praktis",
        "cerdas",
        "tidak menggurui"
    ]
}


with open("output/research_result.json") as f:
    research = json.load(f)


prompt = f"""
Kamu adalah Creative Director dari {brand['name']}.

Brand:
{brand}

Buat ide carousel Instagram berdasarkan research berikut:

{research}

Output wajib JSON:

{{
"title":"",
"target":"",
"hook":"",
"problem":"",
"insight":"",
"slides":[
 {{
 "slide":1,
 "headline":"",
 "body":"",
 "visual_direction":""
 }}
],
"cta":""
}}

Fokus:
- membuat orang berhenti scroll
- meningkatkan save/share
- cocok untuk UMKM dan creator pemula
- bukan konten generik
"""


response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)


result = response.choices[0].message.content


with open("output/ai_carousel.json","w") as f:
    f.write(result)


print("AI Creative Director finished")
