import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values

env = dotenv_values(".env")
openai_client = OpenAI(api_key=env["OPENAI_API_KEY"])

st.title(":brain: Nasz GPT z pamięcią")

def get_chatbot_replay(user_prompt, memory):
# dodaj system message
    messages = [
        {
            "role": "system",
            "content": """
            Jesteś pomocnikiem, który odpowiada na wszystkie pytania użytkownika. Odpowiadaj zwięźle i zrozumiale.
            """
        }
    ]

# dodaj wiadomości z pamięci
    for message in memory:
        messages.append({"role": message["role"], "content": message["content"]})

# dodaj wiadomość użytkownika
    messages.append({"role": "user", "content": user_prompt})

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
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
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state["messages"].append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        chatbot_message = get_chatbot_replay(prompt, memory=st.session_state["messages"][-10:])  # Przekazujemy ostatnie 10 wiadomości jako pamięć
        st.markdown(chatbot_message["content"])

    st.session_state["messages"].append(chatbot_message)


with st.sidebar:
    with st.expander("Historia rozmowy"):
        st.json(st.session_state.get("messages", []))