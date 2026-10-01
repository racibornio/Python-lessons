import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Analiza półmaratonu wrocławskiego 2024')
df = pd.read_csv('halfmarathon_wroclaw_2024__final.csv', sep=';')

# 1. NAJPIERW FILTRACJA (Panel boczny)
with st.sidebar:
    name = st.text_input('Podaj imię zawodnika')
    countries = st.multiselect('Wybierz kraj', sorted(df['Kraj'].dropna().unique()))
    age_categories = st.multiselect('Wybierz kategorię wiekową', sorted(df['Kategoria wiekowa'].dropna().unique()))
    gender = st.radio('Wybierz płeć', options=['Wszystkie', 'Mężczyźni', 'Kobiety'], index=0)

if name:
    df = df[df["Imię"].str.contains(name, case=False, na=False)]

if countries:
    df = df[df["Kraj"].isin(countries)]

if age_categories:
    df = df[df["Kategoria wiekowa"].isin(age_categories)]

if gender == 'Mężczyźni':
    df = df[df["Płeć"] == 'M']
elif gender == 'Kobiety':
    df = df[df["Płeć"] == 'K']

# 2. METRYKI (Liczba zawodników/płeć)
c0, c1, c2, c3 = st.columns(4)

with c0:
    st.metric('Liczba zawodników', len(df))

with c1:
    st.metric('Liczba mężczyzn', len(df[df['Płeć'] == 'M']))

with c2:
    st.metric('Liczba kobiet', len(df[df['Płeć'] == 'K']))

with c3:
    # Poprawiony warunek dla płci nieokreślonej
    st.metric('Płeć nieokreślona', len(df[~df['Płeć'].isin(['M', 'K'])]))

# 3. SECKJA: 10 LOSOWYCH WIERSZY (Zabezpieczona!)
st.header('10 losowych wierszy')
sample_size = min(10, len(df))

if sample_size > 0:
    st.dataframe(df.sample(sample_size), width='stretch', hide_index=True)
else:
    st.warning("Brak danych do wyświetlenia dla wybranych filtrów.")

# 4. TOP 5 ZAWODNIKÓW
st.header('Top 5-ciu zawodników')
top_columns = ["Miejsce", "Numer startowy", "Imię", "Nazwisko", "Miasto", "Płeć", "Kraj", "Czas"]
st.dataframe(df.sort_values(by='Miejsce').head(5)[top_columns], width='stretch', hide_index=True)

# 5. BARPLOT KRAJÓW
st.header('Pochodzenie zawodników')
gdf = df.groupby('Kraj', as_index=False).count().rename(columns={"Miejsce": "Liczba zawodników"})
st.bar_chart(data=gdf, x='Kraj', y='Liczba zawodników')

# 6. HISTOGRAM
st.header('Histogram czasów na mecie')
if len(df) > 0:
    df["Czas_dt"] = pd.to_datetime(df["Czas"], format='%H:%M:%S', errors='coerce')
    minuty = df["Czas_dt"].apply(lambda x: x.hour * 60 + x.minute + x.second / 60 if pd.notnull(x) else None)
    
    plt.figure(figsize=(10, 6))
    plot = sns.histplot(minuty.dropna(), bins=30, kde=True)
    st.pyplot(plot.figure)

# 7. MACIERZ KORELACJI
st.header('Macierz korelacji')
if len(df) > 0:
    correlation_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(16, 12))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, cbar=True)
    st.pyplot(plt.gcf())