from PIL import Image, ImageDraw, ImageFont
import json
import os


print("🖼️ Renderer Agent Started")


with open(
    "output/FINAL_CAROUSEL.json"
) as f:
    carousel = json.load(f)


os.makedirs(
    "output/slides",
    exist_ok=True
)


WIDTH = 1080
HEIGHT = 1350


try:
    headline_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        80
    )

    body_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        40
    )

except:

    headline_font = None
    body_font = None



for slide in carousel["slides"]:

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#111111"
    )


    draw = ImageDraw.Draw(img)


    # orange accent

    draw.rectangle(
        (80,80,150,100),
        fill="#F26B38"
    )


    headline = slide["headline"]


    draw.text(
        (80,200),
        headline,
        font=headline_font,
        fill="#F7F7F5",
        spacing=10
    )


    draw.text(
        (80,900),
        "BOS SONY CREATIVE STUDIO",
        font=body_font,
        fill="#F26B38"
    )


    filename = (
        f"output/slides/"
        f"slide_{slide['slide']:02}.png"
    )


    img.save(filename)


    print(
        "Created:",
        filename
    )


print("✅ Slides rendered")
