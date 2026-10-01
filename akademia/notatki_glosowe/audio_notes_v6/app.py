from io import BytesIO
import streamlit as st
from audiorecorder import audiorecorder
from dotenv import dotenv_values
from openai import OpenAI
from hashlib import md5
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance

env = dotenv_values("../../../.env")

EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIM = 3072
QDRANT_COLLECTION_NAME = "notes"
AUDIO_TRANSCRIBE_MODEL = "whisper-1"

def get_openai_client():
    return OpenAI(api_key=st.session_state["OPENAI_API_KEY"])

def transcribe_audio(audio_bytes):
    openai_client = get_openai_client()
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "audio.mp3"
    transcript = openai_client.audio.transcriptions.create(
        file=audio_file,
        model=AUDIO_TRANSCRIBE_MODEL,
        response_format="verbose_json"
    )

    return transcript.text


# DB

@st.cache_resource
def get_qdrant_client():
    return QdrantClient(path=":memory:")

def assure_db_collection_exists():
    qdrant_client = get_qdrant_client()
    if not qdrant_client.collection_exists(QDRANT_COLLECTION_NAME):
        print(f"Tworzę kolekcję {QDRANT_COLLECTION_NAME}.")
        qdrant_client.create_collection(
            collection_name=QDRANT_COLLECTION_NAME,
            vectors_config=VectorParams(
                size=EMBEDDING_DIM,
                distance=Distance.COSINE
                )
        )
    else:
        print(f"Kolekcja {QDRANT_COLLECTION_NAME} już istnieje.")


def get_embedding(text):
    openai_client = get_openai_client()
    result = openai_client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL,
        dimensions=EMBEDDING_DIM
    )

    return result.data[0].embedding

def add_note_to_db(note_text):
    qdrant_client = get_qdrant_client()
    points_count = qdrant_client.count(
        collection_name=QDRANT_COLLECTION_NAME,
        exact=True
        )

    qdrant_client.upsert(
        collection_name=QDRANT_COLLECTION_NAME,
        points=[
            PointStruct(
                id=points_count.count + 1,
                vector=get_embedding(text=note_text),
                payload=
                {
                    "text": note_text
                 }
            )
            
        ]
    )

def list_notes_from_db(query=None):
    qdrant_client = get_qdrant_client()
    if not query:
        notes = qdrant_client.scroll(collection_name=QDRANT_COLLECTION_NAME, limit=10)[0]
        result = []
        for note in notes:
            result.append({
                "text": note.payload["text"],
                "score" : None
            })
        return result

    else:
        notes = qdrant_client.query_points(
            collection_name=QDRANT_COLLECTION_NAME,
            #query_vector=get_embedding(text=query),
            query=get_embedding(text=query),
            limit=10
        ).points
        result = []
        for note in notes:
            result.append({
                "text": note.payload["text"],
                "score" : note.score
            })
        return result


#

# MAIN

st.set_page_config(page_title="Audio notatki", layout="centered")

# My OpenAI API key protection -- BEGIN
if not st.session_state.get("OPENAI_API_KEY"):
    if "OPENAI_API_KEY" in env:
        st.session_state["OPENAI_API_KEY"] = env["OPENAI_API_KEY"]
    else:
        st.info("Dodaj swój klucz API OpenAI, aby móc korzystać z tej aplikacji.")
        st.session_state["OPENAI_API_KEY"] = st.text_input("Klucz API", type="password")
        if st.session_state["OPENAI_API_KEY"]:
            st.rerun()

if not st.session_state.get("OPENAI_API_KEY"):
    st.stop()
# My OpenAI API key protection -- END


# Session state initialization
if "note_audio_bytes_md5" not in st.session_state:
    st.session_state["note_audio_bytes_md5"] = None

if "note_audio_bytes" not in st.session_state:
    st.session_state["note_audio_bytes"] = None

if "note_text" not in st.session_state:
    st.session_state["note_text"] = ""

if "note_audio_text" not in st.session_state:
    st.session_state["note_audio_text"] = ""


st.title("Witaj na stronie")
assure_db_collection_exists()
add_tab, search_tab = st.tabs(["Dodaj notatkę", "Wyszukaj notatki"])

with add_tab:
    note_audio = audiorecorder(
        start_prompt="Nagraj notatkę",
        stop_prompt="Zatrzymaj nagrywanie"
    )

    if note_audio:
        audio = BytesIO()
        note_audio.export(audio, format="mp3")
        st.session_state["note_audio_bytes"] = audio.getvalue()
        current_md5 = md5(st.session_state["note_audio_bytes"]).hexdigest()
        if st.session_state["note_audio_bytes_md5"] != current_md5:
            st.session_state["note_audio_text"] = ""
            st.session_state["note_text"] = ""
            st.session_state["note_audio_bytes_md5"] = current_md5

        st.audio(st.session_state["note_audio_bytes"], format="audio/mp3")

        if st.button("Transkrybuj audio"):
            st.session_state["note_audio_text"] = transcribe_audio(st.session_state["note_audio_bytes"])

        if st.session_state["note_audio_text"]:
            st.session_state["note_text"] = st.text_area(
                "Edytuj notatkę", value=st.session_state["note_audio_text"]
                )

        if st.session_state["note_text"] and st.button(
            "Zapisz notatkę", disabled=not st.session_state["note_text"]):
            add_note_to_db(note_text=st.session_state["note_text"])
            st.toast("Notatka zapisana w bazie QDrant.", icon="✅")

with search_tab:
    query = st.text_input("Wyszukaj notatki", placeholder="Wpisz tekst do wyszukania")
    if st.button("Pokaż ostatnie notatki"):
        for note in list_notes_from_db(query):
            with st.container(border=True):
                st.markdown(note["text"])
                if note["score"]:
                    st.markdown(f':violet[{note["score"]}]')