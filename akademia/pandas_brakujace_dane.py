from traceback import print_tb

import pandas as pd

df = pd.DataFrame(
    [
        {"name" : "Adam",   "age" : 25,     "city" : "Oława",       "salary" : 7000},
        {"name" : "Bartek", "age" : None,   "city" : "Wrocław",     "salary" : 12000},
        {"name" : "Celina", "age" : 30,     "city" : None,          "salary" : 3200},
        {"name" : "Dorota", "age" : 40,     "city" : "Kraków",      "salary" : None},
        {"name" : "Ewa",    "age" : None,   "city" : "Warszawa",    "salary" : 9000}
    ]
)

print('Wyświetlenie data frame zastanego:')
print(df)
print()

# wyświetl rekordy z brakującymi informacjami
print('Wyświetl rekordy z brakującymi informacjami:')
print(df.isnull())
print()

# wyświetl sumę brakujących wpisów w każdej kolumnie
print('Suma braków w każdej kolumnie:')
print(df.isnull().sum())
print()

# usuń wiersze z brakującymi danymi
print('Usuń wiersze z brakującymi danymi:')
print(df.dropna())
print()
print('Usuń wiersze z brakującymi danymi z axis=1:')
print(df.dropna(axis=1))
print()

# usuń wiersze tylko na podzbiorze kolumny
print('Usuń wiersze tylko na podzbiorze kolumny:')
print(df.dropna(subset="age"))
print()

# wypełnij brakujące dane stałymi wartościami
print('Wypełnij brakujące dane stałymi wartościami:')
print(df.fillna({"age" : 30, "city" : "Unknown", "salary" : 5882}))
print()