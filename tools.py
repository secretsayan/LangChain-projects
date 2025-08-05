# # Tool creation
# tools = [my_tool]
# # Tool binding
# model_with_tools = model.bind_tools(tools)
# # Tool calling
# response = model_with_tools.invoke(user_input)

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply a and b."""
#     return a * b

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")


def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

tools = [multiply]

llm_with_tools = model.bind_tools(tools)
query = "What is 3 multiplied by 12?"
messages = [HumanMessage(query)]
response = llm_with_tools.invoke(messages)

print(f"Message content: {response.text()}\n")
print(f"Tool calls: {response.tool_calls}")

# messages.append(response)
#
#
# for tool_call in response.tool_calls:
#     selected_tool = {"multiply": multiply}[tool_call["name"].lower()]
#     tool_msg = selected_tool.invoke(tool_call)
#     messages.append(tool_msg)
#
# messages

llm_with_tools.invoke(messages)
