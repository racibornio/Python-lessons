import streamlit as st
import pandas as pd
from pathlib import Path
from time import sleep

BASE_DIR = Path(__file__).resolve().parent

st.title("Refresh cycle app")
country = st.selectbox("Wybierz kraj", ["Polska", "Niemcy", "Francja"])

st.write(f'Wybrany kraj: {country}')
df = pd.read_csv(BASE_DIR / "population_gdp_data.csv")
#st.dataframe(df)

[c0, c1] = st.columns(2)
sleep(1)  # symulacja długiej operacji
with c0:
    if country:
        st.image(f'{country.lower()}_kultura.webp',width='stretch')

sleep(1)  # symulacja długiej operacji
country_df = df[df['Kraj'] == country]
with c1:
    st.dataframe(country_df, width='stretch', hide_index=True)

what = st.selectbox("Co narysować?", ['PKB', 'Populacja'])

sleep(1)  # symulacja długiej operacji
st.bar_chart(data=country_df, x='Rok', y=what)