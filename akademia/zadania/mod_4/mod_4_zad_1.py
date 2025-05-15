import pandas as pd
import matplotlib.pyplot as plt

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('25__iris.csv')
print(df)
print()

print('Kolumny:')
print(df.columns)
df.columns = ['Dł_kiel', 'Szer_kiel', 'Dł_płat', 'Szer_płat', 'Klasa']
print()
print('Po zmianie nazw kolumn:')
print(df)
print()

print('Łącznie w każdej klasie jest:')
print(df.groupby('Klasa').size())
print()

print('Unikaty:')
print(df.nunique())
print()

print('Unikatowe klasy:')
print(df['Klasa'].nunique())
print()


# długości kielichów
lista_dlugosci_kielichow = df["Dł_kiel"].to_list()
print('Lista wartości długości kielichów:', lista_dlugosci_kielichow)

dlugosc_kielicha_max = max(lista_dlugosci_kielichow)
print('Najdłuższy kielich:', dlugosc_kielicha_max)

dlugosc_kielicha_min = min(lista_dlugosci_kielichow)
print('Najkrótszy kielich:', dlugosc_kielicha_min)

potencjal_wzrostu_wzdluz = dlugosc_kielicha_max - dlugosc_kielicha_min
procentowy_potencjal_wzrostu_wzdluz = potencjal_wzrostu_wzdluz / dlugosc_kielicha_min * 100
print('Irys wzdłuż może wzrosnąć o', round(potencjal_wzrostu_wzdluz, 1), 'cm, czyli o', round(procentowy_potencjal_wzrostu_wzdluz, 1), 'procent.')
print()


# szerokości kielichów
lista_szerokosci_kielichow = df["Szer_kiel"].to_list()
print('Lista wartości szerokości kielichów:', lista_szerokosci_kielichow)

szerokosci_kielicha_max = max(lista_szerokosci_kielichow)
print('Najszerszy kielich:', szerokosci_kielicha_max)

szerokosci_kielicha_min = min(lista_szerokosci_kielichow)
print('Najwęższy kielich:', szerokosci_kielicha_min)

potencjal_wzrostu_wszerz = szerokosci_kielicha_max - szerokosci_kielicha_min
procentowy_potencjal_wzrostu_wszerz = potencjal_wzrostu_wszerz / szerokosci_kielicha_min * 100
print('Irys wszerz może wzrosnąć o', round(potencjal_wzrostu_wszerz, 1), 'cm, czyli o', round(procentowy_potencjal_wzrostu_wszerz, 1), 'procent.')
print()


# długości płatków - liczone na data frame
najdluzszy_platek = df['Dł_płat'].max()
print('Najdłuższy płatek ma', najdluzszy_platek, 'cm.')

najkrotszy_platek = df['Dł_płat'].min()
print('Najkrótszy płatek ma', najkrotszy_platek, 'cm.')

potencjal_wzrostu_platka_wzdluz = najdluzszy_platek - najkrotszy_platek
procentowy_potencjal_wzrostu_platka_wzdluz = potencjal_wzrostu_platka_wzdluz / najkrotszy_platek * 100
print('Płatek irysa wzdłuż może przyrosnąć o', round(potencjal_wzrostu_platka_wzdluz, 1), 'cm, czyli o', round(procentowy_potencjal_wzrostu_platka_wzdluz, 1), 'procent.')
print()

# szerokości płatków - liczone na data frame
najszerszy_platek = df['Szer_płat'].max()
print('Najszerszy płatek ma', najszerszy_platek, 'cm.')

najwezszy_platek = df['Szer_płat'].min()
print('Najwęższy płatek ma', najwezszy_platek, 'cm.')
potencjal_wzrostu_platka_wszerz = najszerszy_platek - najwezszy_platek
procentowy_potencjal_wzrostu_platka_wszerz = potencjal_wzrostu_platka_wszerz / najwezszy_platek * 100
print('Płatek irysa wszerz może przyrosnąć o', round(potencjal_wzrostu_platka_wszerz, 1), 'cm, czyli o', round(procentowy_potencjal_wzrostu_platka_wszerz, 1), 'procent')
print()

# analiza grup na data frame
print('Zbiorczo - wskaźniki agregujące jako data frame:')
print(
    df.groupby("Klasa")[["Dł_kiel", "Szer_kiel", "Dł_płat", "Szer_płat"]].agg(['min', 'max', 'mean'])
)
print()


# wyliczenie średniej generyczną funkcją
def wylicz_srednia_wymiaru_dla_klasy(wymiar): # przy wywolaniu funkcji jako 'wymiar' podany będzie string wynikowy ze znanej już listy/obiektu kolumn z wywołania df.columns
    # ta zmienna dla podanego wymiaru irysa - dł. lub szer. łodygi, dł. lub szer. kielicha - przechowa średnią dla zadeklarowaneg przy wywołaniu funkcji wymiaru kwiatka
    srednia_wymiaru = df.groupby('Klasa')[wymiar].mean()
    print(srednia_wymiaru) # tu wyświetlamy średnią



# poniższa pętla wywołuje funkcję "wylicz_srednia_wymiaru_dla_klasy", ale najpierw zaglądado struktury "df.columns" i leci po jej pozycjach, które podaje funkcji jako parametry.
# Pomija ostatnią daną "Klasa" bo to jest byt innego typu, stąd -1
for i in range(len(df.columns) - 1):
    wymiar = df.columns[i]
    print('Wyliczam średnią dla:', wymiar)
    wylicz_srednia_wymiaru_dla_klasy(wymiar)
    print()


# wykresy
# histogram

df["Klasa"].hist(bins=5)
plt.show()

# wykres kolowy
df.plot(kind="pie", y="Dł_płat", labels=df['Klasa'], legend=True)
plt.show()

# wykres słupkowy
df.plot(kind="bar", x="Klasa", y=["Dł_kiel", "Dł_płat"])
plt.show()

# wykres punktowy
df.plot(kind="scatter", x="Klasa", y="Dł_kiel")
plt.show()

df.plot(kind="scatter", x="Klasa", y="Szer_kiel")
plt.show()

df.plot(kind="scatter", x="Klasa", y="Dł_płat")
plt.show()

df.plot(kind="scatter", x="Klasa", y="Szer_płat")
plt.show()

# wykres pudełkowy
df.plot(kind="box")
plt.show()