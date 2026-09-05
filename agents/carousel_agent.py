import json

brand = json.load(open("config/brand.json"))

prompt = open(
    "data/prompts/carousel_prompt.txt"
).read()

research = json.load(
    open("output/research_result.json")
)

carousel = {
    "brand": brand["brand"],
    "style": brand["style"],
    "content": [],
    "prompt_template": prompt,
    "research_source": research["topics"]
}

for topic in research["topics"]:
    carousel["content"].append({
        "title": topic["topic"],
        "platform": topic["platform"],
        "slides": [
            "Hook kuat",
            "Masalah audience",
            "Insight",
            "Solusi",
            "CTA"
        ]
    })

with open(
    "output/weekly_carousel.json",
    "w"
) as f:
    json.dump(
        carousel,
        f,
        indent=2
    )

print("Carousel agent finished")
