import zipfile
import os


print("📦 ZIP Export Agent Started")


source_folder = "output/slides"

zip_name = "output/carousel_package.zip"


with zipfile.ZipFile(
    zip_name,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for file in sorted(os.listdir(source_folder)):

        filepath = os.path.join(
            source_folder,
            file
        )

        zipf.write(
            filepath,
            arcname=file
        )


print("✅ ZIP created:")
print(zip_name)
