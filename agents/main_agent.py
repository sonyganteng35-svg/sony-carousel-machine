import subprocess
import os
import json

print("🚀 Bos Sony Carousel Machine V2 Started")


agents = [
    "research_agent.py",
    "creative_director.py",
    "carousel_agent.py",
    "quality_agent.py"
]


for agent in agents:

    print(f"\n▶ Running {agent}")

    result = subprocess.run(
        ["python", f"agents/{agent}"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)


print("\n✅ All agents finished")


os.makedirs("output", exist_ok=True)


final_file = "output/final_carousel.json"


if not os.path.exists(final_file):

    data = {
        "status":"completed",
        "message":"Carousel pipeline finished",
        "brand":"Bos Sony Creative Studio"
    }

    with open(final_file,"w") as f:
        json.dump(data,f,indent=2)


print("🎯 FINAL CAROUSEL READY")
