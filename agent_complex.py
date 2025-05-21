from smolagents import (
    LiteLLMModel,
    CodeAgent, 
    DuckDuckGoSearchTool, 
    UserInputTool
)

model = LiteLLMModel(model_id='ollama/mychen76/qwen3_cline_roocode:8b')
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), UserInputTool()],
    add_base_tools=True,
    model=model,
)


agent.run(str(input("Prompt: ")))

