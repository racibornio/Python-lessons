import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# tytuł aplikacji
st.title("Strona główna - tekst z st.title")
st.title("Kolejny tytuł - tekst z st.title")

# pasek boczny
with st.sidebar:
    st.radio("Select gender:", ['K', 'M'])

# zmiana układu strony
st.set_page_config(layout='wide')

# przycisk wysyłania pliku
uploaded_file = st.file_uploader('Wybierz plik')

# wyświetlenie kodu
st.code("for i in range (3): pętla")

# wyświetlenie obrazka
st.image('Ścieżka do obrazka')

# wykres słupkowy - najpierw stwórz dataframe, potem go przekaż
df = pd.DataFrame({
    'A' : np.random.randint(0, 100, 5),
    'B' : np.random.randint(0, 100, 5)
})
st.bar_chart(df)

# wyszarzenie przycisku
st.button('Kliknij', disabled=True)

# pole tekstowe
wpis = st.text_input("Enter a text")
st.write("Wpisano:", wpis)

# dodanie pliku audio
st.audio('Ścieżka do pliku')

# pole daty
date = st.date_input('Wybierz datę')
st.write('Wpisano:', date)

# dodanie pliku video
st.video('Ścieżka do pliku')

# przycisk
if st.button("Click"):
    st.write('Przycisk kliknięty')

# markdown
st.markdown('''
    To jest **markdown**
''')

# dataframe
st.dataframe(df, hide_index=True)

# informowanie o statusach
st.error('To jest error')
st.warning('To jest warning')
st.info('To jest info')
st.success('To jest sukces')

# pole czasu
time = st.time_input('Podaj czas')
st.write('Wpisano:', time)

# suwak
value = st.slider('Wybierz wartość:', 0, 100, 50)
st.write('Wybrano:', value)

# tekst pomocy
st.text_input('Podaj tekst', help='Tekst pomocy')

# wykres matplotlib
x = np.random.randn(100)
y = np.random.randn(100)

fig, ax = plt.subplots()
ax.scatter(x, y)
st.pyplot(fig)

# przycisk pobierania
st.download_button(
    'Pobierz plik',
    data='''
name, age
Alice, 25
Bob, 30
    ''',
    file_name='data.csv',
    mime="text/csv"
)

# radio-buttony
option = st.radio('Wybierz opcję', ['A', 'B', 'C'])

# checkboxy
wybrane = st.multiselect("Pick a day", ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
st.write('Wybrano:', wybrane)

# użycie kolumn
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.write("Lewa kolumna")

with col2:
    st.write("Prawa kolumna")

with col3:
    st.write("3-cia kolumna")

with col4:
    st.write("4-ta kolumna")

with col5:
    st.write("5-ta kolumna")

with col6:
    st.write("6-ta kolumna")


# pole numeryczne
number = st.number_input('Podaj liczbę')
st.write('Podano:', number)

# pole wyboru
st.selectbox("Pick a day", ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# dodanie metryki
st.metric('Koszt rozmowy (PLN)', 123.45)

# pole tekstowe typu hasło
password = st.text_input('Podaj hasło', type='password')
st.write('Wpisano:', password)

# komponenty czatu
st.chat_input("Element z st.chat_input")
st.chat_message("user")

# tworzenie formularza
with st.form(key='my_form'):
    text_input = st.text_input('Podaj imię')
    submit_button = st.form_submit_button('Wyślij')
    if submit_button:
        st.write('Wpisano:', text_input)



# checkbox
st.checkbox("I agree")
if st.checkbox("I agree"):
    st.write('Zaznaczono zgodę')


# pole wielowierszowe
text = st.text_area('Podaj tekst')
st.write('Wpisano:', text)

# nagłówek
st.header('Nagłówek strony')


# korzystanie z st.session_state
if 'counter' not in st.session_state:
    st.session_state["counter"] = 0

st.write(f"Counter: {st.session_state['counter']}")
if st.button("Increment"):
    st.session_state["counter"] += 1




st.write("Tekst z st.write")

st.html("<h1>Header 1</h1>")

with st.echo():
    st.write("Code from 'echo()' function.")

with st.expander("Rozwiń..."):
    st.write("Pierwsza opcja")
    st.write("Druga opcja")
    st.write("Trzecia opcja")

st.toggle("Enable")
