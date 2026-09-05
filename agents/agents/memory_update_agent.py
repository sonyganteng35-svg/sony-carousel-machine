import json
import os
from datetime import datetime


print("💾 Updating Content Memory")


with open(
    "output/FINAL_CAROUSEL.json"
) as f:

    carousel = json.load(f)


history_file = "memory/content_history.json"


with open(history_file) as f:

    history = json.load(f)



history["published_content"].append(

    {
        "date":
        datetime.now().strftime("%Y-%m-%d"),

        "title":
        carousel.get("title",""),

        "hook":
        carousel.get("hook","")
    }

)



os.makedirs(
    "memory",
    exist_ok=True
)


with open(
    history_file,
    "w"
) as f:

    json.dump(
        history,
        f,
        indent=2
    )


print("✅ Memory updated")
