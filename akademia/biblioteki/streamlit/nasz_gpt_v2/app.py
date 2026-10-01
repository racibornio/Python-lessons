import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values

env = dotenv_values(".env")
openai_client = OpenAI(api_key=env["OPENAI_API_KEY"])

st.title(":black_joker: Nasz GPT z OpenAI")

def get_chatbot_replay(user_prompt):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
            You are a helpful assistant that answers questions in a concise and clear manner."""},
            {"role": "user", "content": user_prompt},
        ]
    )

    return {
        "role" : "assistant",
        "content" : response.choices[0].message.content
    }

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("O co chcesz zapytać papugę?")
if prompt:
    with st.chat_message("human"):
        st.markdown(prompt)

    st.session_state["messages"].append({"role": "human", "content": prompt})


    with st.chat_message("assistant"):
        chatbot_message = get_chatbot_replay(prompt)
        st.markdown(chatbot_message["content"])

    st.session_state["messages"].append(chatbot_message)