from PIL import Image, ImageDraw, ImageFont
import json
import os


print("🎨 Renderer Agent Started")


INPUT = "output/final_carousel.json"
OUTPUT = "output/slides"


os.makedirs(
    OUTPUT,
    exist_ok=True
)


with open(INPUT, "r") as f:
    data = json.load(f)


W = 1080
H = 1350


try:
    headline_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        90
    )

    body_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        42
    )

    number_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        220
    )

except:
    headline_font = None
    body_font = None
    number_font = None



for slide in data["slides"]:

    img = Image.new(
        "RGB",
        (W,H),
        "#111111"
    )

    draw = ImageDraw.Draw(img)


    number = str(
        slide.get("slide_number",1)
    ).zfill(2)


    # BIG NUMBER

    draw.text(
        (760,80),
        number,
        font=number_font,
        fill="#333333"
    )


    # ORANGE ACCENT

    draw.rectangle(
        (80,120,240,140),
        fill="#F26B38"
    )


    # HEADLINE

    draw.text(
        (80,260),
        slide.get(
            "headline",
            ""
        ),
        font=headline_font,
        fill="#F7F7F5"
    )


    # BODY

    draw.text(
        (80,650),
        slide.get(
            "body",
            ""
        ),
        font=body_font,
        fill="#F7F7F5"
    )


    # BRAND

    draw.text(
        (80,1220),
        "BOS SONY CREATIVE STUDIO",
        font=body_font,
        fill="#F26B38"
    )


    filename = (
        OUTPUT +
        "/slide_" +
        number +
        ".png"
    )


    img.save(filename)

    print(
        "created:",
        filename
    )


print(
    "✅ Renderer finished"
)
