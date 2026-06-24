from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


# initiate the model
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

# initiate the 'message' object
message = [
    SystemMessage("Act like a Piriate"),
    HumanMessage("What is the weather like today?"),
]

# execute the model (with message)
result = llm.invoke(message);

# Show result in the screen
print(result.content)