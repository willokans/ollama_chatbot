import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot")

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
        
    # create the echo (response) and add it to the screen
    response = f"You said: {prompt}"
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
        st.session_state.messages.append(AIMessage(content=response))