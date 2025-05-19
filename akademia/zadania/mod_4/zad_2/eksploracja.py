from traceback import print_tb

import pandas as pd

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('26__titanic.csv')
print(df.head(5).to_string())
print()

print('Kolumny:')
print(df.columns)
print()

print('Indeksy:')
print(df.index)
print()

print('Podzbiór losowy:')
print(df.sample(5))
print()

print('Unikaty kolumny Klasa:')
print(df['pclass'].nunique)
print()

print('Policzone unikaty klasy:')
print(df['pclass'].value_counts())
print()

for kolumna in df.columns:
    print('Unikaty dla', kolumna)
    print(df[kolumna].value_counts(dropna=False))
    print()

print()
# oczyszczanie danych
print('Brakujące dane:')
print('Wyświetl czy są rekordy z brakującymi danymi:')
print(df.isnull())
print()

print('Wyświetl sumę brakujących wpisów w każdej kolumnie:')
print(df.isnull().sum())
print()

print('Pokaż data frame po usunięciu wierszy z brakującymi danymi:')
print(df.dropna())
print()

print('Czy zbiór przetrwał?:')
print(df)

print('Tymczasowo wypełnij brakujace dane stałymi:')
print(
    df.fillna(
        {"pclass" : "klasa niewiadoma", "survived" : "nie wiadomo", "name" : "anonim", "sex" : "płeć nieznana", " age" : "wiek nieznany", "sibsp" : "czy rodzina?", "parch" : "czy rodzice/dzieci?", "ticket" : "czy bilet?", "fare" : "jaki przejazd?", "cabin" : "kabina?", "embarked" : "czy wyruszył?", "boat" : "czy łódź?", "body" : "numer ciała", "home.dest" : "skąd/dokąd ?"}
    )
)
print()

print('Totalna suma:')
print(len(df))
print()

print('Liczba wierszy i kolumn:')
print(df.shape)
print()

print('Wierszy:', df.shape[0], ', kolumn:', df.shape[1])
print()