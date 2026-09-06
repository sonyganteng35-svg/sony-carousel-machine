import os
import json
import google.generativeai as genai


print("🤖 Gemini AI Carousel Agent Started")


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


with open("output/creative_plan.json") as f:
    creative = json.load(f)


prompt = f"""
Kamu adalah AI Content Director Bos Sony Creative Studio.

Brand:
Bos Sony Creative Studio

Style:
Creative Editor Culture,
Premium Editorial,
Modern Advertising


Buat Instagram carousel profesional.

Creative direction:
{creative}


Output hanya JSON:

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
"""


response = model.generate_content(prompt)


content = response.text

content = content.replace("```json", "")
content = content.replace("```", "")
content = content.strip()


data = json.loads(content)


with open("output/ai_carousel.json","w") as f:
    json.dump(data,f,indent=2)


print("✅ Gemini generation finished")
