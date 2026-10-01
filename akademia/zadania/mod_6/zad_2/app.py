import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';')

st.header("Witaj na stronie z analizą dataframe!")

with st.expander("Kliknij aby zobaczyć/ukryć surowy dataframe..."):
    st.dataframe(df)

# ============================================================
# 1. NORMALIZACJA DANYCH — ROBIMY TO NA SAMYM POCZĄTKU
# ============================================================

df['years_of_experience'] = (
    df['years_of_experience']
    .astype(str)
    .str.strip()
    .str.replace(" ", "")
    .str.replace("–", "-")
    .str.normalize("NFKC")
)

df['years_of_experience'] = df['years_of_experience'].replace({
    '0–2': '0-2',
    '0 — 2': '0-2',
    '0 – 2': '0-2',
    '3–5': '3-5',
    '6–10': '6-10',
    '11–15': '11-15',
    '≥16': 'pow. 15-tu lat',
    '>=16': 'pow. 15-tu lat',
    '16+': 'pow. 15-tu lat',
    '16lat': 'pow. 15-tu lat',
    '16lat+': 'pow. 15-tu lat',
})

# ============================================================
# 2. DEFINICJA KOLEJNOŚCI — RAZ, NA GÓRZE
# ============================================================

kolejnosc = ['0-2', '3-5', '6-10', '11-15', 'pow. 15-tu lat']

# ============================================================
# 3. WYKRESY GÓRNE
# ============================================================

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

# ============================================================
# 4. SELECTBOX — ULUBIONE MIEJSCA
# ============================================================

st.write("")
miejsca = ['Nad wodą', 'W górach', 'W lesie', 'Inne', 'Nie podano']
wybor = st.selectbox("W jakich miejscach lubimy spędzać czas?", miejsca)
ikony_miejsc = {
    'Nad wodą': '🌊',
    'W górach': '🏔️',
    'W lesie': '🌲',
    'Inne': '⭐',
    'Nie podano': '❓'
}


if wybor == 'Nie podano':
    liczba_osob = df['fav_place'].isna().sum()
else:
    liczba_osob = df[df['fav_place'] == wybor].shape[0]

st.write(f"{ikony_miejsc.get(wybor, '')} {liczba_osob} osób!")

# ============================================================
# 5. SELECTBOX — DOŚWIADCZENIE + WYKRES PROCENTOWY
# ============================================================

st.write("")
przedzialy_raw = df['years_of_experience'].dropna().unique()
przedzialy = [p for p in kolejnosc if p in przedzialy_raw]

wybor = st.selectbox("Wybierz przedział lat doświadczenia:", przedzialy)

df_filtr = df[df['years_of_experience'] == wybor]
liczba_projekty = df_filtr[df_filtr['learning_pref_personal_projects'] == 1].shape[0]

st.write(f"{liczba_projekty} osób rozwija własne projekty.")

# --- WYKRES PROCENTOWY ---
st.write("")
st.write("")
wyniki = []

for p in przedzialy:
    grupa = df[df['years_of_experience'] == p]
    liczba_w_grupie = grupa.shape[0]
    liczba_projekty = grupa[grupa['learning_pref_personal_projects'] == 1].shape[0]

    procent = round(liczba_projekty / liczba_w_grupie * 100) if liczba_w_grupie > 0 else 0
    wyniki.append({"Przedział": p, "Procent rozwijających projekty": procent})

df_wyniki = pd.DataFrame(wyniki)
#st.bar_chart(df_wyniki.set_index("Przedział"))
fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df_wyniki["Przedział"], df_wyniki["Procent rozwijających projekty"], color='cornflowerblue')

ax.set_ylim(0, 100)  # zakres Y do 100%
ax.set_ylabel("Procent rozwijających projekty (%)", fontsize=14)
ax.set_xlabel("Przedział lat doświadczenia", fontsize=14)

plt.xticks(rotation=0, fontsize=12)  # poziomo + większy font
plt.yticks(fontsize=12)

ax.set_title("Procent osób rozwijających własne projekty w zależności od doświadczenia", fontsize=16)

st.pyplot(fig)


# ============================================================
# 6. SIDEBAR — KORZYSTA Z TEJ SAMEJ KOLEJNOŚCI I NORMALIZACJI
# ============================================================

liczba_osob = len(df)
ilu_czyta = df['hobby_books'].sum()
procent_czytajacych = round(ilu_czyta / liczba_osob * 100)

distinct_industry = df['industry'].dropna()
distinct_industry = distinct_industry[distinct_industry != ""]
liczba_branż = distinct_industry.nunique()

lata_doswiadczenia = {
    k: df[df['years_of_experience'] == k].shape[0]
    for k in kolejnosc
}

with st.sidebar:
    st.header("Ciekawostki...")
    st.write(f'Z kursu dotychczas skorzystało {liczba_osob} osób.')
    st.write(f'{ilu_czyta} uczestników, tj. {procent_czytajacych}% czyta książki w ramach hobby!')
    st.write(f'Uczestnicy kursu wywodzą się z {liczba_branż} branż rynkowych.')
    st.write('Doświadczenie rynkowe rozkłada się tak:')
    for przedzial, liczba in lata_doswiadczenia.items():
        st.write(f'{przedzial} → {liczba} osób.')
