import json
import os


print("📈 Feedback Agent Started")


history_file = "memory/performance_history.json"


if os.path.exists(history_file):

    with open(history_file) as f:
        history = json.load(f)

else:

    history = {
        "content_performance":[]
    }


feedback = {

    "metrics": {

        "hook_strength": 0,
        "saveability": 0,
        "shareability": 0,
        "conversion": 0

    },


    "learning": [

        "Perhatikan performa hook slide pertama",

        "Prioritaskan konten problem solving",

        "Gunakan visual before-after"

    ]

}


history["content_performance"].append(
    feedback
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


with open(
    "output/feedback_report.json",
    "w"
) as f:

    json.dump(
        feedback,
        f,
        indent=2
    )


print("✅ Feedback memory updated")
