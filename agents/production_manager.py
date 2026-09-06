import os
import shutil
import json
import zipfile


print("📦 Production Manager Started")


source = "output"

package = "output/Bos_Sony_Carousel_Final"


folders = [
    "01_Content",
    "02_Design",
    "03_Creative"
]


for folder in folders:
    os.makedirs(
        f"{package}/{folder}",
        exist_ok=True
    )


# Content

files_content = {
    "FINAL_CAROUSEL.json":
    "01_Content/carousel.json",

    "caption.txt":
    "01_Content/caption.txt"
}


for src, dst in files_content.items():

    if os.path.exists(
        f"{source}/{src}"
    ):
        shutil.copy(
            f"{source}/{src}",
            f"{package}/{dst}"
        )



# Creative

files_creative = {
    "image_prompts.json":
    "03_Creative/image_prompts.json",

    "canva_brief.json":
    "03_Creative/canva_brief.json"
}


for src, dst in files_creative.items():

    if os.path.exists(
        f"{source}/{src}"
    ):
        shutil.copy(
            f"{source}/{src}",
            f"{package}/{dst}"
        )



# Slides

slide_source = "output/slides"

slide_target = f"{package}/02_Design"


if os.path.exists(slide_source):

    for file in os.listdir(slide_source):

        shutil.copy(
            f"{slide_source}/{file}",
            f"{slide_target}/{file}"
        )



# ZIP

zip_path = "output/FINAL_UPLOAD.zip"


with zipfile.ZipFile(
    zip_path,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for root, dirs, files in os.walk(package):

        for file in files:

            filepath = os.path.join(
                root,
                file
            )

            zipf.write(
                filepath
            )


print(
    "✅ FINAL_UPLOAD.zip created"
)
