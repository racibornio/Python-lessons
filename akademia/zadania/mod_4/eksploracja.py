import pandas as pd
import matplotlib.pyplot as plt

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv(r'C:\\Users\\pos\\Documents\\Python\\Python-lessons\\akademia\\zadania\\mod_4\\25__iris.csv')
print(df)
print()

# zmiana nazw kolumn
df.columns = ['Dł_kiel', 'Szer_kiel', 'Dł_płat', 'Szer_płat', 'Klasa']
print()
print('Po zmianie nazw kolumn:')
print(df)
print()

# średnia dł. kiel.
print('Średnia długości kielicha dla klasy:')
print(
    df.groupby('Klasa')['Dł_kiel'].mean()
)
print()

# średnia szer. kiel.
print('Średnia szerokość kielicha dla klasy:')
print(
    df.groupby('Klasa')['Szer_kiel'].mean()
)
print()

print('Test nazwy kolumny', df.columns[0], df.columns[1])



def wylicz_srednia_wymiaru_dla_klasy(wymiar):
    srednia_wymiaru = df.groupby('Klasa')[wymiar].mean()
    print(srednia_wymiaru)


print('Z wywołania funkcji:')

for i in range(len(df.columns) - 1):
    wymiar = df.columns[i]
    print('Wyliczam średnią dla:', wymiar)
    wylicz_srednia_wymiaru_dla_klasy(wymiar)
    print()