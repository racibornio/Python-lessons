import streamlit as st
import time

with st.sidebar:
    example_name = st.selectbox(
        "Wybierz przykład do pokazania",
        [
            "Progress bar",
            "Spinner",
            "Status",
            "Tosty",
            "Balony",
            "Śnieg",
            "Sukces",
            "Błąd",
            "Wyjątki",
            "Informacja",
            "Ostrzeżenie",
        ],
    )

#
# PROGRESS BAR
#
if example_name == "Progress bar":
    progress_text = "Proszę czekać..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    time.sleep(1)
    my_bar.empty()

    st.button("Uruchom ponownie")

#
# SPINNER
#
if example_name == "Spinner":
    with st.spinner("Czekaj..."):
        time.sleep(5)
    st.success("Gotowe!")

#
# STATUS
#
if example_name == "Status":
    with st.status("Pobieram dane...", expanded=True) as status:
        st.write("Szukam danych...")
        time.sleep(2)
        st.write("Znalazłem URL.")
        time.sleep(1)
        st.write("Pobieram dane...")
        time.sleep(1)
        status.update(label="Pobieranie zakończone!", state="complete", expanded=False)

    st.button("Rerun")

#
# TOAST
#
if example_name == "Tosty":
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hurra!", icon="🎉")

#
# Baloons
#
if example_name == "Balony":
    st.balloons()

#
# Snow
#
if example_name == "Śnieg":
    st.snow()

#
# Success
#
if example_name == "Sukces":
    st.success("Gotowe! Jest sukces")

#
# Error
#
if example_name == "Błąd":
    st.error("Coś poszło nie tak")

#
# Exceptions
#
if example_name == "Wyjątki":
    e = RuntimeError("This is an exception of type RuntimeError")
    st.exception(e)

#
# Info
#
if example_name == "Informacja":
    st.info("To jest informacja")

#
# Warning
#
if example_name == "Ostrzeżenie":
    st.warning("To jest ostrzeżenie")
