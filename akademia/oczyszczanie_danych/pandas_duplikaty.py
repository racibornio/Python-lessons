import pandas as pd
from pandas.core.algorithms import duplicated

df = pd.DataFrame(
    {
        'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Emma', 'Alice', 'Bob'],
        'Age' : [25, 30, 35, 40, 45, 45, 25, 30],
        'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Phoenix', 'New York', 'Los Angeles'],
        'Salary' : [7000, 8000, 90000, 10000, 11000, 12000, 7000, 8000]
    }
)

print('Nowy data frame:')
print(df)
print()

# pokaż duplikaty czy są jakieś duplikaty - True lub False
print('Pokaż duplikaty:')
print(df.duplicated())
print()

# pokaż duplikaty podzbioru - True lub False
print('Pokaż duplikaty podzbioru:')
print(df.duplicated(subset=["Name", "Age", "City"]))
print()

# wyświetl zduplikowane wiersze
print('Wyświetl zduplikowane wiersze:')
print(df[df.duplicated()])
print()

# usuwanie duplikatów - żeby nie wliczały się podwójnie do średniej itp. - usuwa tylko wtedy gdy dokładnie każda kolumna ma takie same wartości
print('Usuń duplikaty, żeby nie zaburzały wyników średniej itp.:')
print(df.drop_duplicates())
print()

# usuwanie duplikatów tylko dla podzbioru
print('Usuń duplikaty tylko dla podzbioru:')
print(df.drop_duplicates(subset=["Name", "Age", "City"]))
print()

# usuń dulikaty, ale pierwsze a zostaw ostatni
print('Usuń duplikaty poprzedzające, a zostaw ostatnie wystąpienie:')
print(df.drop_duplicates(subset=["Name", "Age", "City"], keep="last"))
print()