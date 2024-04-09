from dotenv import load_dotenv
load_dotenv()
import os

import streamlit as st
import google.generativeai as genai

api_key=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

## function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    respone = chat.send_message(question,stream=True)
    return respone

#initialize streamlit app 

st.set_page_config(page_title="Q&A Demo")
st.header ("Gemini LLM Application")
# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state[ 'chat_history'] = []


input=st. text_input ("Input:", key="input")
submit = st.button("Ask the Question")

if submit and input:
    response = get_gemini_response(input)
    ## add user query and response to chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Gemini's Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History : ")

for role,text in st.session_state['chat_history']:
    if role=="You":
        st.write(f"You: {text}")
    else:
        st.write(f"Bot: {text}")
