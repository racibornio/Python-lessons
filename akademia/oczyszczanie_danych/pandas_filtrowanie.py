import pandas as pd

df = pd.DataFrame(
    [
        {"name" : "Adam", "age" : 25, "weight" : 70, "height" : 180},
        {"name" : "Alicja", "age" : 30, "weight" : 60, "height" : 170},
        {"name" : "Bartek", "age" : 35, "weight" : 100, "height" : 160},
        {"name" : "Celina", "age" : 42, "weight" : 55, "height" : 150}
    ],
    index=["pracownik HR 0", "pracownik HR 1", "pracownik IT 0", "pracownik IT 1"]
)

print(df)

# wybranie tylko niektórych kolumn do wyświetlenia
print(df[["name", "age"]])
print()


# wyekstrahowanie wybranych kolumn do nowego data frame
name_and_age_df = df[["name", "age"]].copy()
print('Po stworzeniu nowego, węższego w dane data frame:')
print(name_and_age_df)
print()

# podniesienie roku o 1
name_and_age_df["age"] += 1
print('Po zwiększeniu wieku o 1:')
print(name_and_age_df)
print()

# podaj tylko rekordy spełniające warunek
print('Tylko osoby pow. 40-go r.ż.:')
print(df["age"] > 40)
print()

# podaj tylko rekordy spełniające warunki
print('Tylko osoby pow. 40-go r.ż. i 150cm:')
print((df["age"] > 40) & (df["height"] > 150) )
print()

# podaj tylko rekordy spełniające warunki
print('Tylko osoby pow. 40-go r.ż. lub 150cm:')
print((df["age"] > 40) | (df["height"] > 150) )
print()

# podaj rekord o podanym id
print('Rekord o podanym id - tutaj 1:')
print(df.iloc[1])
print()

# podaj rekordy o podanych id
print('Rekord o podanym id - tutaj zakres:')
print(df.iloc[0:3])
print()

# podaj wpis o konkretnej wartości indeksu
print('Rekord po wartości string indeksu:')
print(df.loc["pracownik IT 0"])
print()

nowy_slownik = {"k1" : "v1", "k2" : ""}
print('Nowy słownik:')
print(nowy_slownik)
print()

print('Nowa lista słowników:')
nowa_lista_slownikow = [
    {"d1 k1" : "d1 v1", "d1 k2" : "d1" "v2"},
    {"d2 k1": "d2 v1", "d2 k2": "d2" "v2"}
]
print(nowa_lista_slownikow)
print()

nowy_df = pd.DataFrame(nowa_lista_slownikow)
print('Lista słowników jako data frame:')
print(nowy_df)

lista_slownikow_jednakowych_kluczy = [
    {"k1" : "k1v1", "k2" : "k1v2"},
    {"k1" : "k2v1", "k2" : "k2v2"},
    {"k1" : "", "k2" : "k2v2"}
]

rownolegly_slownik_df = pd.DataFrame(lista_slownikow_jednakowych_kluczy)
print('Lista słowników jednakowych kluczy:')
print(rownolegly_slownik_df)
print()

# filtrowanie po wartości, której nie ma na liście - czyli wyklucz tych z podanej tu listy i wtedy zwróć wartości pozostające
print('Filtrowanie po wartości, której nie ma na liście:')
print('Jeszcze raz czysty data frame:')
print(df)
print('Teraz filtrowanie:')
print(df[~df["name"].isin(['Adam', 'Celina'])])
print()

# teraz przeciwnie - filtrowanie tylko po wartościach, które są w przekazanej liście
print('Teraz przeciwnie - filtrowanie tylko po wartościach, które występują w przekazanej liście:')
df = df[df["name"].isin(['Adam', 'Celina'])]
print(df)
print()

# filtrowanie data frame po dacie
print('Filtrowanie po dacie:')
daty_df = pd.DataFrame([
    {"date" : "2021-01-01"},
    {"date" : "2021-02-01"}
])
daty_df["date"] = pd.to_datetime(daty_df["date"])
print(daty_df[daty_df["date"] > "2021-01-15"])
print()