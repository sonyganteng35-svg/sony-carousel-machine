from PIL import Image
import os


input_folder = "output/slides"
output_folder = "output/final_upload"


os.makedirs(
    output_folder,
    exist_ok=True
)


for file in os.listdir(input_folder):

    if file.endswith(".png"):

        path = os.path.join(
            input_folder,
            file
        )

        img = Image.open(path)

        # paksa ukuran IG
        img = img.resize(
            (1080,1350)
        )


        # convert RGB
        if img.mode != "RGB":
            img = img.convert("RGB")


        output = os.path.join(
            output_folder,
            file.replace(
                ".png",
                ".jpg"
            )
        )


        img.save(
            output,
            quality=90,
            optimize=True
        )


        print(
            "optimized:",
            output
        )


print("DONE")
