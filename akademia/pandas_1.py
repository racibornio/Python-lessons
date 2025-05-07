import pandas as pd
import random

# zad. 1 - powstaje data frame
df = pd.DataFrame([
    {"D1 k1": "D1 v1", "D1 k2": "D1 v2"},
    {"D2 k1": "D2 v1", "D2 k2": "D2 v2"},
    {"D3 k1": "D3 v1", "D3 k2": "D3 v2"}
],
    index = ['1st', '2nd', '3rd']
)

print(df)
print(df.columns)
print(df.index)


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

# pokaż unikaty
print('unikatowe:')
print(df.nunique())
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

# zmiana nazwy kolumny
print('Zmiana nazwy kolumny:')
df = df.rename(columns={"name" : "Imię"})
print(df)
print()