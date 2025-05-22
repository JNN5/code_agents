from strands import Agent
from strands.models.ollama import OllamaModel

from strands_tools import calculator, current_time, python_repl, shell, editor, http_request
from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient

# Connect to an MCP server using stdio transport
stdio_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"])
))

# Create an agent with MCP tools
with stdio_mcp_client:
    # Get the tools from the MCP server
    mcp_tools = stdio_mcp_client.list_tools_sync()
    # Create an Ollama model instance
    ollama_model = OllamaModel(
        host="http://localhost:11434",  # Ollama server address
        model_id="Default",               # Specify which model to use
        tools=[calculator, current_time, python_repl, shell, editor, http_request] + mcp_tools,
    )

    # Create an agent using the Ollama model
    agent = Agent(model=ollama_model)

    # Use the agent
    prompt = input("Prompt: ")
    agent(prompt) # Prints model output to stdout by default