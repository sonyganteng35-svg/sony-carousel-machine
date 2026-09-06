from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json
import os


print("🎨 Master Carousel Renderer Started")


W = 1080
H = 1350


BLACK = (17,17,17)
WHITE = (247,247,245)
ORANGE = (242,107,56)
GRAY = (51,51,51)


os.makedirs(
    "output/final_carousel",
    exist_ok=True
)


with open(
    "output/FINAL_CAROUSEL.json"
) as f:
    carousel = json.load(f)



try:
    headline_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        85
    )

    body_font = ImageFont.truetype(
        "DejaVuSans.ttf",
        38
    )

    number_font = ImageFont.truetype(
        "DejaVuSans-Bold.ttf",
        180
    )

except:
    headline_font = None
    body_font = None
    number_font = None



for slide in carousel["slides"]:

    number = slide["slide"]

    img_path = (
        f"output/slides/"
        f"slide_{number}.png"
    )


    canvas = Image.new(
        "RGB",
        (W,H),
        BLACK
    )


    if os.path.exists(img_path):

        photo = Image.open(
            img_path
        ).convert("RGB")


        photo.thumbnail(
            (W,900)
        )


        canvas.paste(
            photo,
            (
                0,
                450
            )
        )


    draw = ImageDraw.Draw(canvas)


    # number

    draw.text(
        (70,60),
        f"{number:02}",
        fill=GRAY,
        font=number_font
    )


    # brand

    draw.text(
        (70,250),
        "BOS SONY",
        fill=ORANGE,
        font=headline_font
    )


    draw.text(
        (70,340),
        "CREATIVE STUDIO",
        fill=WHITE,
        font=headline_font
    )


    headline = slide.get(
        "headline",
        ""
    )


    draw.text(
        (70,560),
        headline,
        fill=WHITE,
        font=headline_font
    )


    body = slide.get(
        "body",
        ""
    )


    draw.text(
        (70,850),
        body,
        fill=WHITE,
        font=body_font
    )


    # accent line

    draw.rectangle(
        (
            70,
            1180,
            400,
            1190
        ),
        fill=ORANGE
    )


    draw.text(
        (70,1220),
        "BOS SONY CREATIVE STUDIO",
        fill=WHITE,
        font=body_font
    )


    output = (
        f"output/final_carousel/"
        f"slide_{number}_final.png"
    )


    canvas.save(output)


    print(
        "Created:",
        output
    )



print(
"✅ Final carousel rendered"
)
