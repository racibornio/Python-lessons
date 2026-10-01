import streamlit as st

st.title("Notatki")

if "notatki" not in st.session_state:
    st.session_state["notatki"] = []

notatka = st.text_area("Wpisz notatkę", height=100, max_chars=200)

if st.button("Dodaj notatkę"):
    st.session_state["notatki"].append(notatka.strip())

st.write(st.session_state["notatki"])

st.metric("Liczba notatek", len(st.session_state["notatki"]))

with st.expander("Rozwiń/Ukryj notatki"):
    st.json(st.session_state["notatki"])

if st.button("Wyczyść notatki"):
    st.session_state["notatki"] = []
    st.success("Notatki zostały wyczyszczone z pamięci sesji.")
    st.rerun()  # Przeładuj aplikację, aby odświeżyć stan notatek


if st.button("Zapisz notatki"):
    with open("notatki.txt", "a") as f:
        notatki_txt = "\n".join(st.session_state["notatki"])
        f.write(f"\n{notatki_txt}")

    st.session_state["notatki"] = []
    st.success("Notatki zostały zapisane do pliku notatki.txt i wyczyszczone z pamięci sesji.")
    st.rerun()  # Przeładuj aplikację, aby odświeżyć stan notatek