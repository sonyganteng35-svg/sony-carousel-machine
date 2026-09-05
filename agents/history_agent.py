import json
import os


print("📚 Content History Agent Started")


history_file = "memory/content_history.json"


if os.path.exists(history_file):

    with open(history_file) as f:
        history = json.load(f)

else:

    history = {
        "published_content": []
    }


context = {

    "total_content":
    len(history["published_content"]),

    "previous_topics":
    [
        item["title"]
        for item in history["published_content"]
    ]

}


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/content_memory.json",
    "w"
) as f:

    json.dump(
        context,
        f,
        indent=2
    )


print("✅ Content memory loaded")
