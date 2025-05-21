from smolagents import (
    MLXModel,
    CodeAgent, 
    DuckDuckGoSearchTool, 
)

# model = MLXModel(model_id="mlx-community/SmolLM2-1.7B-Instruct")
# model = MLXModel(model_id="mlx-community/Mamba-Codestral-7B-v0.1")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen2.5-Coder-7B-Instruct-abliterated-v1")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen2.5-3B-Instruct-abliterated-v1-8-bit")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen3-4B-abliterated-v1-8bit")
# model = MLXModel(model_id="mlx-community/gemma-3-4b-it-4bit-DWQ")
model = MLXModel(model_id="mlx-community/gemma-3-12b-it-4bit-DWQ")
prompt = "How many seconds would it take for a leopard at full speed to run through Pont des Arts?"

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    add_base_tools=True,
    model=model,
)

agent.run(prompt)