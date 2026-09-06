import os
import json
import shutil


print("📦 Final Package Agent Started")


package = "output/Bos_Sony_Carousel_Package"


os.makedirs(
    package,
    exist_ok=True
)


os.makedirs(
    f"{package}/slides",
    exist_ok=True
)


# Copy slides

source_slides = "output/slides"

if os.path.exists(source_slides):

    for file in os.listdir(source_slides):

        shutil.copy(
            f"{source_slides}/{file}",
            f"{package}/slides/{file}"
        )


# Copy carousel JSON

if os.path.exists(
    "output/FINAL_CAROUSEL.json"
):

    shutil.copy(
        "output/FINAL_CAROUSEL.json",
        f"{package}/carousel.json"
    )


# Caption generator placeholder

with open(
    f"{package}/caption.txt",
    "w"
) as f:

    f.write(
"""Caption Instagram:

Tambahkan caption hasil AI carousel di sini.

#BosSonyCreativeStudio
#ContentCreator
#VideoEditing
"""
    )


with open(
    f"{package}/upload_checklist.txt",
    "w"
) as f:

    f.write(
"""UPLOAD CHECKLIST

☑ Slide ukuran 1080x1350
☑ Hook slide pertama kuat
☑ Caption tersedia
☑ CTA tersedia
☑ Visual konsisten brand
"""
    )


print(
"✅ Final package created"
)
