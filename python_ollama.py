from langchain_ollama import ChatOllama
from langchain.core.messages import SystemMessage, HummanMessage


# initiate the model
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

# initiate the 'message' object
message = [
    SystemMessage("Act like a Piriate"),
    HummanMessage("What is the weather like today?")
]

# execute the model (with message)
result = llm.invoke(message);

# Show result in the screen
print(result)