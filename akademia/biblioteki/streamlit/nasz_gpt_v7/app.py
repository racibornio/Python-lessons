
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
        messages.append({
            "role": message["role"],
            "content": message["content"]
        })

# dodaj wiadomość użytkownika
    messages.append({
        "role": "user",
        "content": user_prompt
    })

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



DEFAULT_PERSONALITY = """
Jesteś pomocnikiem, który odpowiada na wszystkie pytania użytkownika. Odpowiadaj zwięźle i zrozumiale.
""".strip()

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "db"
DB_CONVERSATIONS_PATH = DB_PATH / "conversations"

def load_conversation_to_state(conversation):
    st.session_state["id"] = conversation.get("id")
    st.session_state["name"] = conversation.get("name")
    st.session_state["messages"] = conversation.get("messages", [])
    st.session_state["chatbot_personality"] = conversation.get("chatbot_personality", DEFAULT_PERSONALITY)


def load_current_conversation():
    if not DB_PATH.exists():
        DB_PATH.mkdir()
        DB_CONVERSATIONS_PATH.mkdir()
        conversation_id = 1
        conversation = {
                "id" : conversation_id,
                "name" : "Konwersacja 1",
                "chatbot_personality" : DEFAULT_PERSONALITY,
                "messages" : []
            }

        with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w") as f:
            f.write(json.dumps(conversation))

        with open(DB_PATH / "current.json", "w") as f:
            f.write(json.dumps({
                "current_conversation_id" : conversation_id
            }))


    else:
        with open(DB_PATH / "current.json", "r") as f:
            data = json.loads(f.read())
            conversation_id = data["current_conversation_id"]

        with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r") as f:
            conversation = json.loads(f.read())

    load_conversation_to_state(conversation)


def save_current_conversation_messages():
    conversation_id = st.session_state.get("id")
    new_messages = st.session_state.get("messages", [])

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r") as f:
        conversation = json.loads(f.read())

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w") as f:
        f.write(json.dumps({
            **conversation,
            "messages": new_messages
        }))


def save_current_conversation_name():
    conversation_id = st.session_state.get("id")
    new_conversation_name = st.session_state["new_conversation_name"]

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r") as f:
        conversation = json.loads(f.read())

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w") as f:
        f.write(json.dumps({
            **conversation,
            "name": new_conversation_name
        }))


def save_current_conversation_personality():
    conversation_id = st.session_state.get("id")
    new_chatbot_personality = st.session_state["new_chatbot_personality"]

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r") as f:
        conversation = json.loads(f.read())

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w") as f:
        f.write(json.dumps({
            **conversation,
            "chatbot_personality": new_chatbot_personality
        }))


def create_new_conversation():
    conversation_ids = []
    for p in DB_CONVERSATIONS_PATH.glob("*.json"):
        conversation_ids.append(int(p.stem))

    conversation_id = max(conversation_ids) + 1

    personality = DEFAULT_PERSONALITY
    if "chatbot_personality" in st.session_state and st.session_state["chatbot_personality"]:
        personality = st.session_state["chatbot_personality"]

    conversation = {
        "id" : conversation_id,
        "name" : f"Konwersacja {conversation_id}",
        "chatbot_personality" : personality,
        "messages" : []
    }

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w") as f:
        f.write(json.dumps(conversation))

    with open(DB_PATH / "current.json", "w") as f:
        f.write(json.dumps({
            "current_conversation_id" : conversation_id
        }))

    load_conversation_to_state(conversation)
    st.rerun()


def switch_conversation(conversation_id):
    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r") as f:
        conversation = json.loads(f.read())

    with open(DB_PATH / "current.json", "w") as f:
        f.write(json.dumps({
            "current_conversation_id" : conversation_id
        }))

    load_conversation_to_state(conversation)
    st.rerun()


def list_conversations():
    conversations = []
    for p in DB_CONVERSATIONS_PATH.glob("*.json"):
        with open(p, "r") as f:
            conversation = json.loads(f.read())
            conversations.append({
                "id": conversation["id"],
                "name": conversation["name"],
                })

    return conversations

load_current_conversation()

st.title(":classical_building: Nasz GPT")

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("O co chcesz zapytać papugę?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state["messages"].append({
        "role": "user",
        "content": prompt
    })


    with st.chat_message("assistant"):
        chatbot_message = get_chatbot_replay(prompt, memory=st.session_state["messages"][-10:])  # Przekazujemy ostatnie 10 wiadomości jako pamięć
        st.markdown(chatbot_message["content"])

    st.session_state["messages"].append(chatbot_message)
    save_current_conversation_messages()


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

    st.session_state["name"] = st.text_input(
        "Nazwa konwersacji",
        value=st.session_state["name"],
        key="new_conversation_name",
        on_change=save_current_conversation_name
    )

    st.session_state["chatbot_personality"] = st.text_area(
        "Ustaw osobowość chatbota",
        height=200,
        max_chars=1000,
        value = st.session_state["chatbot_personality"],
        on_change=save_current_conversation_personality
    )


    st.subheader("Konwersacje")
    if st.button("Nowa konwersacja"):
        create_new_conversation()

    conversations = list_conversations()
    sorted_conversations = sorted(conversations, key=lambda x: x["id"], reverse=True)
    for conversation in sorted_conversations[:5]:
        c0, c1 = st.columns([10, 3])
        with c0:
            st.write(f"{conversation['name']}")
        with c1:
            if st.button("Załaduj", key=conversation["id"], disabled=conversation["id"] == st.session_state["id"]):
                switch_conversation(conversation["id"])
