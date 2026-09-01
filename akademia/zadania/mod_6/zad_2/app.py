import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';')

st.header("Witaj na stronie z analizą dataframe!")

with st.expander("Kliknij aby zobaczyć/ukryć surowy dataframe..."):
    st.dataframe(df)


col1, col2, col3 = st.columns(3)

with col1:
    zwierzeta = df['fav_animals'].dropna().value_counts()
    fig1, ax1 = plt.subplots()
    ax1.bar(zwierzeta.index, zwierzeta.values, color='skyblue')
    ax1.set_title('Ulubione zwierzęta')
    ax1.set_xlabel('Zwierzę')
    ax1.set_ylabel('Liczba osób')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with col2:
    miejsca = df['fav_place'].dropna().value_counts()
    fig2, ax2 = plt.subplots()
    ax2.bar(miejsca.index, miejsca.values, color='lightgreen')
    ax2.set_title('Ulubione miejsca spędzania czasu wolnego')
    ax2.set_xlabel('Miejsce')
    ax2.set_ylabel('Liczba osób')
    plt.xticks(rotation=45)
    st.pyplot(fig2)

with col3:
    df_psy = df[df['fav_animals'] == 'Psy']
    miejsca_psy = df_psy['fav_place'].dropna().value_counts()
    fig3, ax = plt.subplots()
    ax.bar(miejsca_psy.index, miejsca_psy.values, color='orange')
    ax.set_title('Gdzie właściciele psów lubią spędzać czas')
    ax.set_xlabel('Miejsce')
    ax.set_ylabel('Liczba osób')
    plt.xticks(rotation=45)
    st.pyplot(fig3)


liczba_osob = len(df)

ilu_czyta = df['hobby_books'].sum()
procent_czytajacych = round(ilu_czyta/liczba_osob*100)

distinct_industry = df['industry'].dropna()
distinct_industry = distinct_industry[distinct_industry != ""]
liczba_branż = distinct_industry.nunique()

df['years_of_experience'] = (
    df['years_of_experience']
    .astype(str)
    .str.strip()
    .str.replace(" ", "")
    .str.replace("–", "-")
    .str.normalize("NFKC")
)

lata_doswiadczenia = (
    df['years_of_experience']
    .replace(["", "nan", "NaN"], None)
    .dropna()
    .value_counts()
    .to_dict()
)

kolejnosc = ['0-2', '3-5', '6-10', '11-15', '\>=16']

lata_doswiadczenia_sorted = {
    k: lata_doswiadczenia.get(k, 0)
    for k in kolejnosc
}

with st.sidebar:
    st.header("Ciekawostki...")
    st.write(f'Z kursu dotychczas skorzystało {liczba_osob} osób.')
    st.write(f'{ilu_czyta} uczestników, tj. {procent_czytajacych}% czyta książki w ramach hobby!')
    st.write(f'Uczestnicy kursu wywodzą się z {liczba_branż} branż rynkowych.')
    st.write('Doświadczenie rynkowe rozkłada się tak:')
    for przedzial, liczba in lata_doswiadczenia_sorted.items():
        st.write(f'{przedzial} -> {liczba} osób.')
