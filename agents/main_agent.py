import subprocess


print("🚀 Bos Sony Carousel Machine FINAL")


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

    print(
        f"Running {agent}"
    )

    subprocess.run(
        [
            "python",
            f"agents/{agent}"
        ]
    )


print(
    "✅ FINAL CAROUSEL GENERATED"
)
