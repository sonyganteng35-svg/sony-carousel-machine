import subprocess
import os

print("🚀 Bos Sony Carousel Machine Started")

print("Step 1: Running Research Agent")
subprocess.run(
    ["python", "agents/research_agent.py"]
)

print("Step 2: Running Carousel Agent")
subprocess.run(
    ["python", "agents/carousel_agent.py"]
)

print("✅ Carousel generation finished")

print(
    "Output saved in output/weekly_carousel.json"
)
