import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_ai(prompt):

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": 
                "Kamu adalah Creative Director Bos Sony Creative Studio. Buat ide konten Instagram carousel yang menarik, praktis, dan conversion oriented."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
