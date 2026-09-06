import os
import zipfile


print("📦 ZIP Export Agent Started")


source_folder = "output/slides"

zip_name = "output/Bos_Sony_Carousel.zip"


if not os.path.exists(source_folder):
    print("❌ Slides folder belum ada")
    exit()


with zipfile.ZipFile(
    zip_name,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for root, dirs, files in os.walk(source_folder):

        for file in files:

            path = os.path.join(
                root,
                file
            )

            zipf.write(
                path,
                arcname=file
            )


print(
    "✅ ZIP created:",
    zip_name
)
