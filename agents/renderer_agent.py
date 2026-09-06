from PIL import Image, ImageDraw, ImageFont
import json
import os


print("🎨 Premium Carousel Renderer Started")


# Load final carousel data
with open(
    "output/FINAL_CAROUSEL.json"
) as f:
    carousel = json.load(f)


output_folder = "output/slides"

os.makedirs(
    output_folder,
    exist_ok=True
)


W = 1080
H = 1350


# colors
BLACK = (17,17,17)
WHITE = (247,247,245)
ORANGE = (242,107,56)
GRAY = (51,51,51)


try:
    headline_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        80
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



slides = carousel.get(
    "slides",
    []
)


for index, slide in enumerate(slides):

    img = Image.new(
        "RGB",
        (W,H),
        BLACK
    )


    draw = ImageDraw.Draw(img)


    # slide number

    draw.text(
        (70,80),
        f"{index+1:02}",
        font=number_font,
        fill=GRAY
    )


    # brand

    draw.text(
        (80,250),
        "BOS SONY\nCREATIVE STUDIO",
        font=headline_font,
        fill=ORANGE
    )


    headline = slide.get(
        "headline",
        "Creative Content"
    )


    body = slide.get(
        "body",
        ""
    )


    draw.text(
        (80,520),
        headline,
        font=headline_font,
        fill=WHITE
    )


    draw.text(
        (80,760),
        body,
        font=body_font,
        fill=WHITE
    )


    # footer

    draw.rectangle(
        (80,1220,1000,1228),
        fill=ORANGE
    )


    path = (
        f"{output_folder}/"
        f"slide_{index+1:02}.png"
    )


    img.save(path)


    print(
        "Created:",
        path
    )


print(
    "✅ All carousel slides rendered"
)
