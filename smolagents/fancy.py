from smolagents import (
    MLXModel,
    CodeAgent, 
    DuckDuckGoSearchTool,
    VisitWebpageTool,
)

# model = MLXModel(model_id="mlx-community/gemma-3-12b-it-4bit-DWQ")
model = MLXModel(model_id="mlx-community/Qwen2.5-Coder-14B-Instruct-4bit")

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(),VisitWebpageTool()],
    add_base_tools=True,
    model=model,
    additional_authorized_imports=["requests", "markdownify", "numpy", "datetime"],
)


prompt = input("Prompt: ")
#  I will be travelling to London in exactly 30 days for one week. Please calculate a budget for me that includes flights, airport transfer in london and a hotel that ha is located within a 10km radius of buckingham palace
agent.run(prompt)

# matplotlib