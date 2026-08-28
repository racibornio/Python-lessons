import pandas as pd
import streamlit as st

df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';')

st.header("Witaj na stronie z analizą dataframe!")

with st.expander("Kliknij aby zobaczyć/ukryć surowy dataframe..."):
    st.dataframe(df)


liczba_osob = len(df)
ilu_czyta = df['hobby_books'].sum()
procent_czytajacych = round(ilu_czyta/liczba_osob*100)

with st.sidebar:
    st.header("Ciekawostki...")
    st.write(f'Z kursu dotychczas skorzystało {liczba_osob} osób.')
    st.write(f'{ilu_czyta} uczestników, tj. {procent_czytajacych} % czyta książki w ramach hobby!')