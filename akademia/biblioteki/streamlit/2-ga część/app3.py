import streamlit as st
from random import randint
from time import sleep


st.title("Aplikacja z długim czasem obliczeń")

def calculate_ai_reply(min_value, max_value):
    sleep(10)
    return randint(min_value, max_value)


with st.form("moj formularz", border=False):
    min_value = st.slider("Wybierz minimalną wartość", 0, 100, 0)
    max_value = st.slider("Wybierz maksymalną wartość", 0, 100, 100)

    if st.form_submit_button("Oblicz"):
        if min_value > max_value:
            st.error("Minimalna wartość nie może być większa od maksymalnej wartości!")

        else:
            result = calculate_ai_reply(min_value, max_value)
            st.metric("Wynik", result)
