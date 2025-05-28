from smolagents import (
    LiteLLMModel,
    CodeAgent, 
    DuckDuckGoSearchTool,
    tool 
)

model = LiteLLMModel(model_id='ollama/hf.co/unsloth/Seed-Coder-8B-Instruct-GGUF:Q4_K_M', num_ctx=32768) 

@tool
def calculate_total_cost(activity_cost: float) -> float:
    """
    Calculates the total cost of the itinerary.
    Args:
        activity_cost (float): The cost of the activity.
    """
    return activity_cost + 10.0  # Assuming a fixed transport cost of 10.0 SGD

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), calculate_total_cost],
    add_base_tools=True,
    model=model,
    stream_outputs=True
)

activity = input("What type of activity would you prefer? E.g. Adventure, Relaxation, Culture or Entertainment: ")
date_and_time= input("When would you like to do this activity: E.g. Tonight, Saturday morning, December holidays, etc: ")
budget = input("What is a budget you have in mind: E.g. 50 SGD, 100 SDG, etc: ")

prompt = """
You are a travel agent in Singapore. 
I am looking for a {activity} activity to do on {date_and_time} in Singapore. 
My budget is {budget}. Please suggest some options. 
Here are some hints:
1. Do research first
2. Make sure to find out the proce for each option and include it in your response.
Please also calculate the total cost of the itinerary including transport costs.
""".format(
    activity=activity,
    date_and_time=date_and_time,
    budget=budget
)
agent.run(prompt)