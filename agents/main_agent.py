import subprocess
import sys


print("🚀 Bos Sony Carousel Machine Started")


agents = [

    "research_agent.py",

    "creative_director.py",

    "carousel_agent.py",

    "visual_agent.py",

    "quality_agent.py",

    "renderer_agent.py",

    "zip_agent.py"

]


for agent in agents:

    print("\n======================")
    print("Running:", agent)
    print("======================")


    result = subprocess.run(
        [
            sys.executable,
            f"agents/{agent}"
        ]
    )


    if result.returncode != 0:

        print(
            "❌ Failed:",
            agent
        )

        exit(1)



print("")
print("======================")
print("✅ CAROUSEL COMPLETE")
print("======================")
print("")
print("Check:")
print("output/slides/")
print("output/Bos_Sony_Carousel.zip")
