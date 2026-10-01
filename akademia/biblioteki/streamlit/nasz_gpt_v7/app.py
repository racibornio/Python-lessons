
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
    # Upewniamy się, że katalogi istnieją
    DB_PATH.mkdir(parents=True, exist_ok=True)
    DB_CONVERSATIONS_PATH.mkdir(parents=True, exist_ok=True)

    current_file = DB_PATH / "current.json"

    # Jeśli brak pliku current.json, zaczynamy od od nowa
    if not current_file.exists():
        create_new_conversation()
        return

    # Odczytujemy ID z current.json
    try:
        with open(current_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            conversation_id = data.get("current_conversation_id", 1)
    except (json.JSONDecodeError, KeyError):
        conversation_id = 1

    target_conversation_file = DB_CONVERSATIONS_PATH / f"{conversation_id}.json"

    # JEŚLI PLIK KONWERSACJI NIE ISTNIEJE – tworzymy nową zamiast wyrzucać błąd!
    if not target_conversation_file.exists():
        create_new_conversation()
        return

    # Odczytujemy właściwy plik konwersacji
    with open(target_conversation_file, "r", encoding="utf-8") as f:
        conversation = json.load(f)

    load_conversation_to_state(conversation)


def save_current_conversation_messages():
    conversation_id = st.session_state.get("id")
    new_messages = st.session_state.get("messages", [])

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r", encoding="utf-8") as f:
        conversation = json.load(f)

    conversation["messages"] = new_messages

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=4, ensure_ascii=False)


def save_current_conversation_name():
    conversation_id = st.session_state.get("id")
    new_conversation_name = st.session_state.get("new_conversation_name")

    if not conversation_id or not new_conversation_name:
        return

    # Aktualizujemy stan główny
    st.session_state["name"] = new_conversation_name

    # Zapisujemy do pliku
    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r", encoding="utf-8") as f:
        conversation = json.loads(f.read())

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w", encoding="utf-8") as f:
        json.dump({
            **conversation,
            "name": new_conversation_name
        }, f, indent=4, ensure_ascii=False)


def save_current_conversation_personality():
    conversation_id = st.session_state.get("id")
    new_chatbot_personality = st.session_state.get("new_chatbot_personality", DEFAULT_PERSONALITY)

    st.session_state["chatbot_personality"] = new_chatbot_personality

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "r", encoding="utf-8") as f:
        conversation = json.load(f)

    conversation["chatbot_personality"] = new_chatbot_personality

    with open(DB_CONVERSATIONS_PATH / f"{conversation_id}.json", "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=4, ensure_ascii=False)


def create_new_conversation():
    # 1. Pobieramy wszystkie istniejące ID z plików w katalogu db/conversations/
    conversation_ids = []
    for p in DB_CONVERSATIONS_PATH.glob("*.json"):
        if p.stem.isdigit():
            conversation_ids.append(int(p.stem))

    # 2. Jeśli są już pliki, bierzemy największe ID + 1. Jeśli nie ma – zaczynamy od 1.
    new_id = max(conversation_ids) + 1 if conversation_ids else 1

    # 3. Ustalamy osobowość chatbota
    personality = st.session_state.get("chatbot_personality", DEFAULT_PERSONALITY)

    # 4. Tworzymy obiekt nowej konwersacji
    new_conversation = {
        "id": new_id,
        "name": f"Konwersacja {new_id}",
        "chatbot_personality": personality,
        "messages": []
    }

    # 5. Tworzymy NOWY plik JSON dla tej konkretnej konwersacji (np. 2.json, 3.json...)
    with open(DB_CONVERSATIONS_PATH / f"{new_id}.json", "w", encoding="utf-8") as f:
        json.dump(new_conversation, f, indent=4, ensure_ascii=False)

    # 6. Aktualizujemy plik current.json, aby wskazywał na nowo utworzone ID
    with open(DB_PATH / "current.json", "w", encoding="utf-8") as f:
        json.dump({"current_conversation_id": new_id}, f, indent=4)

    # 7. Ładujemy nową konwersację do session_state i odświeżamy aplikację
    load_conversation_to_state(new_conversation)
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
    
    # Obliczanie kosztów
    total_cost = 0
    for message in st.session_state.get("messages", []):
        if "usage" in message and message["usage"]:
            total_cost += message["usage"].get("prompt_tokens", 0) / 1_000_000 * PRICING["prompt_tokens"]
            total_cost += message["usage"].get("completion_tokens", 0) / 1_000_000 * PRICING["completion_tokens"]

    c0, c1 = st.columns(2)
    with c0:
        st.metric("Koszt w USD", f"${total_cost:.4f}")
    with c1:
        st.metric("Koszt w PLN", f"{total_cost * USD_TO_PLN:.4f}")

    # Nazwa konwersacji
    st.text_input(
        "Nazwa konwersacji",
        value=st.session_state.get("name", ""),
        key="new_conversation_name",
        on_change=save_current_conversation_name
    )

    # Osobowość chatbota
    st.text_area(
        "Ustaw osobowość chatbota",
        height=200,
        max_chars=1000,
        value=st.session_state.get("chatbot_personality", DEFAULT_PERSONALITY),
        key="new_chatbot_personality",
        on_change=save_current_conversation_personality
    )

    st.subheader("Konwersacje")
    
    # Przycisk tworzenia nowej konwersacji
    if st.button("Nowa konwersacja"):
        create_new_conversation()

    # Lista ostatnich konwersacji
    conversations = list_conversations()
    sorted_conversations = sorted(conversations, key=lambda x: x["id"], reverse=True)
    
    for conversation in sorted_conversations[:5]:
        col_name, col_btn = st.columns([10, 3])
        with col_name:
            st.write(f"{conversation['name']}")
        with col_btn:
            is_current = (conversation["id"] == st.session_state.get("id"))
            if st.button("Załaduj", key=f"btn_{conversation['id']}", disabled=is_current):
                switch_conversation(conversation["id"])