# import streamlit as st
# import google.generativeai as genai
# API_KEY = st.secrets["GEMINI_API_KEY"]
# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel('gemini-1.5-flash')

# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])

# st.title("Chatbot - Your AI Assistant")
# st.write("This is a chatbot made by Tripura.......")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("Say something..."):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     response = st.session_state.chat.send_message(prompt)

#     st.session_state.messages.append({"role": "assistant", "content": response.text})
#     with st.chat_message("assistant"):
#         st.markdown(response.text)
        
import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Chatbot - Your AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

