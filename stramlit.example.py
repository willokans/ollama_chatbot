import streamlit as st

# create the input from
prompt = st.chat_input("Say something to the assistant...")

# if input provided, add it to screen
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        st.markdown(f"You said: {prompt}")