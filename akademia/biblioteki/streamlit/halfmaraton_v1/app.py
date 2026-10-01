import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Analiza półmaratonu wrocławskiego 2024')
df = pd.read_csv('halfmarathon_wroclaw_2024__final.csv', sep=';')
#st.dataframe(df)

# liczba zawodników
c0, c1, c2, c3 = st.columns(4)

with c0:
    st.metric('Liczba zawodników', len(df))

# liczba mężczyzn
with c1:
    st.metric('Liczba mężczyzn', len(df[df['Płeć'] == 'M']))

# liczba kobiet
with c2:
    st.metric('Liczba kobiet', len(df[df['Płeć'] == 'K']))

# płeć nieokreślona
with c3:
    st.metric('Płeć nieokreślona', len(df[df['Płeć'] != 'M']) & len(df[df['Płeć'] != 'K']))

# 10 losowych wiersy
st.header('10 losowych wierszy')
st.dataframe(df.sample(10), width='stretch', hide_index=True)

# top 5-ciu zawodników
st.header('Top 5-ciu zawodników')
top_columns = ["Miejsce", "Numer startowy", "Imię", "Nazwisko", "Miasto", "Płeć", "Kraj", "Czas"]
st.dataframe(df.sort_values(by='Miejsce').head(5)[top_columns], width='stretch', hide_index=True)

# bartplot krajów
st.header('Pochodzenie zawodników')
gdf = df.groupby('Kraj', as_index=False).count().rename(columns={"Miejsce": "Liczba zawodników"})
st.bar_chart(data=gdf, x='Kraj', y='Liczba zawodników')

# histogram czas na mecie
st.header('Histogram czasów na mecie')
df["Czas"] = pd.to_datetime(df["Czas"], format='%H:%M:%S', errors='coerce').dt.time

# toworzenie histogramu przy użyciu seaborn
plt.figure(figsize=(10, 6))
plot = sns.histplot(df["Czas"].apply(lambda x: x.hour * 60 + x.minute + x.second / 60), bins=30, kde=True)
st.pyplot(plot.figure)

# macierz korelacji
st.header('Macierz korelacji')
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, cbar=True)
st.pyplot(plt.gcf())