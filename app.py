import streamlit as st
import google.generativeai as genai 
 

st.title("Welcome to GEN-AI")

genai.configure(api_key="AIzaSyCDweEA7wX16dm2or59HI-49o7LaciLKIw")

text = st.text_input("Enter your prompt")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Submit"):
    response = chat.send_message(text)
    st.write(response.text)