import streamlit as st
import pandas as pd

DATA = 'welcome_survey_simple_v1.csv'

@st.cache_data
def get_all_participants():
    all_df = pd.read_csv(DATA, sep=';')
    return all_df

with st.sidebar:
    st.header("Powiedz coś o sobie")
    st.markdown("Wypełnij poniższy formularz, aby znaleźć osoby o podobnych zainteresowaniach.")
    age = st.selectbox("Wiek", options=['<18', '18-24', '25-34', '35-44', '45-54', '55-65', '>65'])
    edu_level = st.selectbox("Poziom wykształcenia", options=['Podstawowe', 'Średnie', 'Wyższe'])
    fav_animals = st.selectbox("Ulubione zwierzęta", options=['Pies', 'Kot', 'Ptak', 'Ryby', 'Gady', 'Inne', 'Brak'])
    fav_places = st.selectbox("Ulubione miejsca", options=['Plaża', 'Góry', 'Miasto', 'Wieś', 'Inne', 'Brak'])
    gender = st.radio("Płeć", options=['Kobieta', 'Mężczyzna'])

    person_df = pd.DataFrame([
        {
            'age': age,
            'edu_level': edu_level,
            'fav_animals': fav_animals,
            'fav_places': fav_places,
            'gender': gender
        }
    ])

st.write("Twoje dane:")
st.dataframe(person_df, hide_index=True)

all_df = get_all_participants()
st.write("Dostępne dane uczestników:")
st.dataframe(all_df.sample(10   ), hide_index=True)