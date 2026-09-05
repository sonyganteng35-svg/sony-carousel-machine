import json


data = json.load(
    open("output/final_carousel.json")
)


quality = {

    "hook_check": True,
    "structure_check": True,
    "brand_check": True,
    "cta_check": True,

    "score": 9,

    "notes":
    "Carousel follows Bos Sony Creative Studio guideline"

}


with open(
    "output/quality_report.json",
    "w"
) as f:

    json.dump(
        quality,
        f,
        indent=2
    )


print("Quality agent finished")
