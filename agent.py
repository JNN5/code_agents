from smolagents import (
    MLXModel,
    CodeAgent, 
    DuckDuckGoSearchTool, 
)

# model = MLXModel(model_id="mlx-community/SmolLM2-1.7B-Instruct")
model = MLXModel(model_id="mlx-community/Mamba-Codestral-7B-v0.1")
# model = MLXModel(model_id="mlx-community/Mamba-Codestral-7B-v0.1")
prompt = "How many seconds would it take for a leopard at full speed to run through Pont des Arts?"

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    add_base_tools=True,
    model=model,
)

agent.run(prompt)