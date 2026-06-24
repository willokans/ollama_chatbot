import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama

st.title("Chatbot with Ollama")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
            
# create the bar where the can type messages
prompt = st.chat_input("Say something to the assistant...")

# did the use submit a prompt
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        
        st.session_state.messages.append(HumanMessage(content=prompt))
        
    llm = ChatOllama(
        model="llama3.2:3b",
    )
        
    # create the echo (response) and add it to the screen
    result = llm.invoke(st.session_state.messages).content
    
    with st.chat_message("assistant"):
        st.markdown(result)
        
        st.session_state.messages.append(AIMessage(content=result))