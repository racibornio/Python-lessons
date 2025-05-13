import pandas as pd

slownik_list = {
    "l1k1" : ["l1p1", "l1p2"],
    "l2k2" : ["l2p1", "l2p2"]
}

print('Słownik list:')
print(slownik_list)
print('Pierwsza wartość:')
print(slownik_list["l1k1"][0])
print('Ostatnia wartość:')
print(slownik_list["l2k2"][-1])
print()

lista_slownikow = [
    { "s1k1" : "s1w1" , "s1k2" : "s1w2" },
    { "s2k1" : "s2w1" , "s2k2" : "s2w2"}
]

print('Lista słowników:')
print(lista_slownikow)
print('Pierwsza wartość:')
print(lista_slownikow[0]["s1k1"])
print('Ostatnia wartość:')
print(lista_slownikow[-1]["s2k2"])
print()

struktura_zagniezdzona = [
    {"klucz1" :
         [
             {"klucz2-1" :
                  ["lista1", "lista2"]
              },
             {"klucz2-2" :
                  ["lista3", "lista4"]
             }
         ]
    }
]
print('Struktura zagnieżdżona:')
print(struktura_zagniezdzona)
print('Pierwszy element (powinno być "lista1"):')
print(struktura_zagniezdzona[0]["klucz1"][0]["klucz2-1"][0])
print('Ostatni element (powinno być "lista4"):')
print(struktura_zagniezdzona[0]["klucz1"][1]["klucz2-2"][-1])
print()

lista_slownikow_z_brakami = [
    {"k1" : "v1"},
    {"k2" : None},
    {"k3" : "v3"}
]
df_lista = pd.DataFrame(lista_slownikow_z_brakami)
print('Lista słowników z brakującymi danymi:')
print(lista_slownikow_z_brakami)
print('Lista słowników jako data frame:')
print(df_lista)
print('Same brakujące dane - df.isnull():')
print(df_lista.isnull())
print('Suma braków:')
print(df_lista.isnull().sum())
print('Usuń wiersze z brakującymi danymi:')
df_lista_po_usunieciu_pustych = df_lista.dropna()
print(df_lista_po_usunieciu_pustych)
print()

slownik_list_z_brakami = {
    1: [1, 2],
    2: [3, None],
    3: None
}
print('Słownik list z brakami:')
print(slownik_list_z_brakami)
df_slownik = pd.DataFrame(slownik_list_z_brakami)
print('Słownik list jako data frame:')
print(df_slownik)
print('Same brakujące dane - df.isnull():')
print(df_slownik.isnull())
print('Suma braków:')
print(df_slownik.isnull().sum())
print()

pelny_slownik_list = [
    {"producent" : "Toyota", "model" : "Auris", "pojemność" : 1.8},
    {"producent": "Seat", "model": "Ibiza", "pojemność": 1.4},
    {"producent": "Toyota", "model": None, "pojemność": None}
]
print('Pełny słownik list:')
print(pelny_slownik_list)
print()
pelny_slownik_list_df = pd.DataFrame(pelny_slownik_list)
print('Pełny słownik list jako data frame:')
print(pelny_slownik_list_df)
print('Które puste:')
print(pelny_slownik_list_df.isnull())
print('Policz puste:')
print(pelny_slownik_list_df.isnull().sum())
print('Usuń puste:')
print(pelny_slownik_list_df.dropna())
print('Wyświetl ponownie całość:')
print(pelny_slownik_list_df)
print('Kopia do modyfikacji.')
pelny_slownik_list_df_2 = pelny_slownik_list_df.copy()
print('Wypełnij puste zdefiniowanymi wartościami:')
print(pelny_slownik_list_df_2.fillna({"model" : "Aygo", "pojemność" : 1.5}))
print('Wypełnij braki średnią z istniejących:')
pelny_slownik_list_df_2["pojemność"] = pelny_slownik_list_df_2["pojemność"].fillna(pelny_slownik_list_df_2["pojemność"].mean())
print(pelny_slownik_list_df_2)