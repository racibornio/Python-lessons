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