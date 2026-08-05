import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values
import json
from pathlib import Path

model_pricings = {
    "gpt-4o-mini": {
        "prompt_tokens": 0.15,
        "completion_tokens": 0.6
    }
}
MODEL = "gpt-4o-mini"
USD_TO_PLN = 4.5
PRICING = model_pricings[MODEL]


env = dotenv_values(".env")
openai_client = OpenAI(api_key=env["OPENAI_API_KEY"])

st.title(":floppy_disk: Nasz GPT pamięta rozmowę")

def get_chatbot_replay(user_prompt, memory):
# dodaj system message
    messages = [
        {
            "role": "system",
            "content": st.session_state["chatbot_personality"]
        }
    ]

# dodaj wiadomości z pamięci
    for message in memory:
        messages.append({"role": message["role"], "content": message["content"]})

# dodaj wiadomość użytkownika
    messages.append({"role": "user", "content": user_prompt})

    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }

    return {
        "role" : "assistant",
        "content" : response.choices[0].message.content,
        "usage" : usage
    }


if "messages" not in st.session_state:
    if Path("current_conversation.json").exists():
        with open("current_conversation.json", "r") as f:
            chatbot_conversation = json.load(f)
            
            st.session_state["messages"] = chatbot_conversation.get("messages", [])
            st.session_state["chatbot_personality"] = chatbot_conversation.get("chatbot_personality", "")
    else:
            st.session_state["chatbot_personality"] = []

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

    with open("current_conversation.json", "w") as f:
        f.write(json.dumps({
            "chatbot_personality": st.session_state["chatbot_personality"],
            "messages": st.session_state["messages"]
        }))


with st.sidebar:
    st.write("Aktualny model to:", MODEL)
    total_cost = 0
    for message in st.session_state.get("messages", []):
        if "usage" in message:
            total_cost += message["usage"]["prompt_tokens"] / 1_000_000 * PRICING["prompt_tokens"]
            total_cost += message["usage"]["completion_tokens"] / 1_000_000 * PRICING["completion_tokens"]

    c0, c1 = st.columns(2)
    with c0:
        st.metric("Koszt w USD", f"${total_cost:.4f}")
    with c1:
        st.metric("Koszt w PLN", f"{total_cost * USD_TO_PLN:.4f}")

    st.session_state["chatbot_personality"] = st.text_area(
        "Ustaw osobowość chatbota",
        height=200,
        max_chars=1000,
        value="""Jesteś pomocnikiem, który odpowiada na wszystkie pytania użytkownika. Odpowiadaj zwięźle i zrozumiale.""".strip()
    )