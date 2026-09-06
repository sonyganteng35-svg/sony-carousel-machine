import subprocess
import os


print("🚀 Bos Sony Carousel Machine V3 Started")


agents = [
    "research_agent.py",
    "creative_director.py",
    "carousel_agent.py",
    "quality_agent.py",
    "visual_agent.py",
    "renderer_agent.py"
]


for agent in agents:

    print(
        f"\n▶ Running {agent}"
    )

    result = subprocess.run(
        [
            "python",
            f"agents/{agent}"
        ]
    )

    if result.returncode != 0:
        print(
            f"❌ Failed: {agent}"
        )
        exit(1)


print("\n✅ All agents completed")

print(
    "📂 Check output/slides/"
)
