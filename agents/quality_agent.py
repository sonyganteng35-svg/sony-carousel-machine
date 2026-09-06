import json
import os


print("🔍 Quality Check Started")


with open(
    "output/FINAL_CAROUSEL.json"
) as f:
    carousel = json.load(f)


score = 0
issues = []


slides = carousel.get(
    "slides",
    []
)


# Check jumlah slide

if len(slides) >= 6:
    score += 2
else:
    issues.append(
        "Jumlah slide kurang dari 6"
    )


# Check hook

hook = slides[0].get(
    "headline",
    ""
)


if len(hook) > 20:
    score += 2
else:
    issues.append(
        "Hook terlalu lemah"
    )


# Check visual prompt

visual_ok = True

for slide in slides:

    if not slide.get(
        "visual_prompt"
    ):
        visual_ok = False


if visual_ok:
    score += 2
else:
    issues.append(
        "Visual prompt kosong"
    )


# Check CTA

last = slides[-1].get(
    "headline",
    ""
)


if "follow" in last.lower() or "mulai" in last.lower():
    score += 2
else:
    issues.append(
        "CTA belum kuat"
    )


# Final score

report = {

    "score":
    score,

    "status":
    "approved" if score >= 6 else "revise",

    "issues":
    issues
}


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/quality_report.json",
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=2
    )


print(
    "Score:",
    score
)

print(
    report["status"]
)
