import json
import os


print("🧠 Brand Memory Agent Started")


with open(
    "config/brand_memory.json"
) as f:

    brand = json.load(f)


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/brand_context.json",
    "w"
) as f:

    json.dump(
        brand,
        f,
        indent=2
    )


print("✅ Brand memory loaded")
