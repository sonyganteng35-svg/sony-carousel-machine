import subprocess
import os


print("🚀 Bos Sony Carousel Machine Started")


print("\nSTEP 1 — Running Research Agent")

subprocess.run(
    [
        "python",
        "agents/research_agent.py"
    ]
)


print("\nSTEP 2 — Running Creative Director Agent")

subprocess.run(
    [
        "python",
        "agents/creative_director.py"
    ]
)


print("\nSTEP 3 — Running Carousel Writer Agent")

subprocess.run(
    [
        "python",
        "agents/carousel_agent.py"
    ]
)


print("\nSTEP 4 — Checking Output")

if os.path.exists("output"):

    print(
        "\nGenerated files:"
    )

    for file in os.listdir("output"):
        print(
            "-",
            file
        )

else:

    print(
        "Output folder not found"
    )


print(
    "\n✅ Carousel generation finished"
)
