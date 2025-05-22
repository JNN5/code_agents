from smolagents import (
    MLXModel,
    CodeAgent, 
    DuckDuckGoSearchTool, 
)

# model = MLXModel(model_id="mlx-community/Qwen2.5-Coder-14B-Instruct-4bit")
model = MLXModel(model_id="mlx-community/gemma-3-12b-it-4bit-DWQ")

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    add_base_tools=True,
    model=model,
)


activity = input("What type of activity would you prefer? E.g. Adventure, Relaxation, Culture or Entertainment: ")
date_and_time= input("When would you like to do this activity: E.g. Tonight, Saturday morning, December holidays, etc: ")
budget = input("What is a budget you have in mind: E.g. 50 SGD, 100 SDG, etc: ")

prompt = """
You are a travel agent in Singapore. 
I am looking for a {activity} activity to do on {date_and_time} in Singapore. 
My budget is {budget}. Please suggest some options. 
Please specifically list, the itinaries with the total cost per option.
Follow the format below:
1. Option 1: 
   - Itinerary: 
   - Total Cost:
2. Option 2:
   - Itinerary: 
   - Total Cost:
3. Option 3:
   - Itinerary: 
   - Total Cost:
""".format(
    activity=activity,
    date_and_time=date_and_time,
    budget=budget
)
agent.run(prompt)