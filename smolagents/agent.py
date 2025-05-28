from smolagents import (
    LiteLLMModel,
    CodeAgent, 
    DuckDuckGoSearchTool, 
)

# model = MLXModel(model_id="mlx-community/SmolLM2-1.7B-Instruct")
# model = MLXModel(model_id="mlx-community/Mamba-Codestral-7B-v0.1")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen2.5-Coder-7B-Instruct-abliterated-v1")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen2.5-3B-Instruct-abliterated-v1-8-bit")
# model = MLXModel(model_id="mlx-community/Josiefied-Qwen3-4B-abliterated-v1-8bit")
# model = MLXModel(model_id="mlx-community/gemma-3-4b-it-4bit-DWQ")
# model = MLXModel(model_id="mlx-community/gemma-3-12b-it-4bit-DWQ")
# model = MLXModel(model_id="mlx-community/Qwen2.5-Coder-14B-Instruct-4bit")
model = LiteLLMModel(model_id='ollama/hf.co/unsloth/Qwen2.5-Coder-14B-Instruct-128K-GGUF:Q4_K_M', num_ctx=4096) 
prompt = """How many seconds would it take for a leopard at full speed to run through Pont des Arts?"""

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    stream_outputs=True
)

agent.run(prompt)