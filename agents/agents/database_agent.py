import json
import os
from datetime import datetime


print("🗄 Database Agent Started")


database_file = "database/content_database.json"


with open(
    database_file
) as f:
    database = json.load(f)


if os.path.exists(
    "output/FINAL_CAROUSEL.json"
):

    with open(
        "output/FINAL_CAROUSEL.json"
    ) as f:

        carousel = json.load(f)


    record = {

        "date":
        datetime.now().strftime("%Y-%m-%d"),

        "title":
        carousel.get(
            "title",
            "Untitled"
        ),

        "platform":
        "Instagram",

        "status":
        "generated",

        "quality":
        "checked",

        "file":
        "carousel_package.zip"

    }


    database["contents"].append(
        record
    )


with open(
    database_file,
    "w"
) as f:

    json.dump(
        database,
        f,
        indent=2
    )


print("✅ Content database updated")
