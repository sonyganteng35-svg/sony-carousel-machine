import subprocess


print("🚀 Bos Sony Carousel Machine Started")


print("Step 1: Research Agent")

subprocess.run(
    ["python","agents/research_agent.py"]
)


print("Step 2: AI Creative Director")

subprocess.run(
    ["python","agents/ai_agent.py"]
)


print("Step 3: Carousel Agent")

subprocess.run(
    ["python","agents/carousel_agent.py"]
)


print("✅ Carousel generation finished")
