import getpass
import os
from langchain_tavily import TavilySearch

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")


# Add search.
search = TavilySearch(max_results=2)
# search_results = search.invoke("What is the weather in Kolkata")
# print(search_results)
tools = [search]

# memory to store conversation.
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()

# Bind tools with model.
# model_with_tools = model.bind_tools(tools)


# Test first interaction
# query = "What is the weather in Kolkata"
# response = model_with_tools.invoke([{"role": "user", "content": query}])
#
# print(f"Message content: {response.text()}\n")
# print(f"Tool calls: {response.tool_calls}")

# Creating the agent.
from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(model, tools, checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

# Run the agent
input_message = {"role": "user", "content": "Will bitcoin price increase today?"}
# response = agent_executor.invoke({"messages": [input_message]})

# for message in response["messages"]:
#     message.pretty_print()


for step in agent_executor.stream({"messages": [input_message]}, config, stream_mode="values"):
    step["messages"][-1].pretty_print()
