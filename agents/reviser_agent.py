import json
import os


print("🔧 Reviser Agent Started")


with open(
    "output/FINAL_CAROUSEL.json",
    "r"
) as f:
    carousel = json.load(f)


with open(
    "output/quality_report.json",
    "r"
) as f:
    quality = json.load(f)



score = quality["total_score"]


if score >= 8:
    print("✅ Score bagus, tidak perlu revisi")

    carousel["status"] = "approved"

else:

    print("⚠️ Score rendah, melakukan revisi")


    carousel["slides"][0]["headline"] = (
        "Stop bikin konten yang terlihat murah."
    )


    carousel["slides"][0]["body"] = (
        "Ini alasan kenapa video kamu tidak menarik perhatian."
    )


    carousel["slides"][-1]["headline"] = (
        "Follow Bos Sony Creative Studio untuk belajar bikin konten lebih profesional"
    )


    carousel["status"] = "revised"



os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/FINAL_CAROUSEL_V2.json",
    "w"
) as f:
    json.dump(
        carousel,
        f,
        indent=2
    )


print(
    "Revision finished"
)
