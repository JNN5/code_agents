from smolagents import (
    LiteLLMModel,
    CodeAgent, 
    DuckDuckGoSearchTool
)

model = LiteLLMModel(model_id='ollama/hf.co/unsloth/Seed-Coder-8B-Instruct-GGUF:Q4_K_M', num_ctx=32768) 

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    add_base_tools=True,
    model=model,
    stream_outputs=True
)

prompt = input("Ask me anything!: ")
agent.run(prompt)