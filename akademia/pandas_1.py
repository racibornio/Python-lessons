import pandas as pd
import random

# wyświetl absolutnie wszystkie kolumny
pd.options.display.max_columns = None

# zad. 1 - powstaje data frame
df = pd.DataFrame([
    {"D1 k1": "D1 v1", "D1 k2": "D1 v2"},
    {"D2 k1": "D2 v1", "D2 k2": "D2 v2"},
    {"D3 k1": "D3 v1", "D3 k2": "D3 v2"}
],
    index = ['1st', '2nd', '3rd'] # dodawane dla lepszej czytelności
)
print()

# wyświetlenie wartości po uprzednio przypisanym indeksie
print('Wyświetlenie wartości po uprzednio przypisanym indeksie:')
tylko_1_st = df.loc['1st']
print(tylko_1_st)
print()

print('Wyświetlenie całej struktury:')
print(df)

# wyświetl kolumny
print('Kolumny:')
print(df.columns)
print()

# wyświetl index czyli etykiety wierszy, jak id w DB
print('Indeks:')
print(df.index)
print()


# zad. 2 - lista na dane losowe - eksploracja
random_data = []

#dodanie 100 rekordów
for i in range(100):
    random_data.append({
        "name" : random.choice(["Adam", "Ada", "Basia", "Jan", "Kasia"]),
        "age" : random.randint(18, 88),
        "height" : random.randint(150, 200),
        "city" : random.choice(["Wrocław", "Warszawa", "Szczecin", "Kraków", "Praga"])
    })


df = pd.DataFrame(random_data)
print(df)
print()

# pokaż tylko 5 pierwszych
print('Pierwsze - domyślnie 5:')
print(df.head())
print()

# pokaż tylko x pierwszych
print('Pierwsze - custom 9:')
print(df.head(9))
print()

# pokaż tylko 5 ostatnich
print('Ostatnie - domyślnie 5:')
print(df.tail())
print()

# pokaż tylko 2 ostatnie
print('Ostatnie 2:')
print(df.tail(2))
print()

# pokaż jakieś losowe - 1
print('Sample:')
print(df.sample())
print()

# pokaż 10 losowych - uruchom kilka razy dla zrandomizowania wniosków
print('sample 10:')
print(df.sample(10))
print()

# pokaż informacje o kolumnach
print('info:')
print(df.info)
print()

# opisz data frame
print('description:')
print(df.describe())
print()

# policz unikaty
print('Policz unikaty:')
print(df.nunique())
print()

# pokaż unikaty konkretnej kolumny
print('Unikaty samej kolumny age:')
print(df['age'].unique())
print()

#pokaż wartości unikatów i ich liczbę
print('Pokaż wartości unikatów i liczbę ich wystąpień:')
print(df['age'].value_counts())
print()

# pokaż ile razy dana wartość występuje w kolumnie
print('Po ile razy występują:')
print(df["name"].value_counts())
print()

# zad. 3 - operacja na data frame
df = pd.DataFrame([
    {"name" : "Adam", "age" : 25, "weight" : 70, "height [cm]" : 180},
    {"name" : "Alicja", "age" : 30, "weight" : 60, "height [cm]" : 170},
    {"name" : "Bartek", "age" : 35, "weight" : 100, "height [cm]" : 160}
])

print('Data frame z 3-go zadania:')
print(df)
print()
print('Wieki:')
print(df["age"])
print()

#dodanie kolumny
df["country"] = "Poland"
print('Data frame po dodaniu kolumny "country" - wszędzie jest wartość "Poland":')
print(df)

# dodanie kolumny, która wyliczy coś z innych kolumn
df["height [m]"] = df["height [cm]"] / 100
print('Nowa kolumna będąca ilorazem innej - wzrost [m]:')
print(df)
print()

# dodanie kolumny będącej wyliczeniem dwóch innych
df["bmi"] = df["weight"] / (df["height [cm]"] / 100) ** 2
print('Nowa kolumna z operacji na dwóch innych kolumnach')
print(df)
print()

# dodanie kolumny będącej wynikiem działania funkcji
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


print('Dodanie kolumny z kategoryzacją bmi - wynikiem działania funkcji')
df["bmi category"] = df["bmi"].apply(bmi_category)
print(df)
print()


# usunięcie kolumn
df.drop(columns="height [m]", inplace=True)
print('Data frame po usunięciu kolumny "height [m]":')
print(df)
print()


# nadpisanie wartości w kolumnie
print('Nadpisanie wartości w kolumnie:')
df["age"] += 1
print(df)
print()



# zmiana nazwy kolumny - gdy tylko niektóre to słownikiem
print('Zmiana nazwy kolumny:')
df = df.rename(columns={"name" : "Imię"})
print(df)
print()

# alternatywnie - nie trzeba nadpisywać zmiennej gdy damy inplace=True
print('Zmiana nazw wielu kolumn - słownikiem:')
df.rename(columns={"age" : "Wiek",
                   "weight" : "Waga [kg]",
                   "height [cm]" : "Wzrost [cm]",
                   "country" : "Kraj",
                   "bmi" : "BMI",
                   "bmi category" : "Zaszeregowanie"
                   },
          inplace=True)

print(df)
print()

#zmiana nazwy kolumn wg kolejności występowania
print('Zmiana nazw wszytkich kolumn - listą:')
df.columns = ['Imię', 'Wiek', 'Waga', 'Wzrost', 'Kraj', 'BMI', 'Klasyfikacja']
print(df)
print()

# zmiana kolejności kolumn - zwykłe wpisanie pożądanej kolejności na nowo do df

# sortowanie po kolumnie - rosnąco i malejąco
print()
print('Sortowanie rosnąco:')
print(df.sort_values(by="Wzrost"))
print()
print('Sortowanie malejąco:')
print(df.sort_values(by="Wzrost", ascending=False))
print()


# usunięcie konkretnej kolumny
print('Kolumny teraz:')
print(df.columns)
print('Usuwamy klasyfikację')
df = df.drop('Klasyfikacja', axis=1)
print(df.columns)
print()

# próbny słownik na test niejednowymiarowości
lista_slownikow = [
    { "k1-1" : "v1-1" },
    { "k2-1" : "v2-1", "k2-2" : "v2-2" },
    { "k3-1" : "v3-1", "k3-2" : "v3-2", "k3-3" : "v3-3"}
]

print('Próbna lista słowników niejednowymiarowych')
print(lista_slownikow)
print()

print('Wrzucenie tej listy do data frame')
lista_slownikow_df = pd.DataFrame(lista_slownikow)
print(lista_slownikow_df)