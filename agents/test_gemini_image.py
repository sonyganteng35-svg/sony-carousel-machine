import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[
        """
        Create a premium Instagram carousel visual.

        Brand:
        Bos Sony Creative Studio

        Style:
        Creative Editor Culture,
        Premium Editorial,
        Modern Advertising.

        Visual:
        Creator working at a modern editing workstation,
        cinematic lighting,
        black and orange color accent,
        vertical 4:5,
        no text,
        no watermark.
        """
    ]
)


print(response)
