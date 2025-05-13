import pandas as pd
# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.DataFrame(
    {
        'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
        'Hire Date' : ['2024-07-15', '2019-07-23', '2018-03-14', '2021-06-01', '2017-11-30', '2022-02-15', '2019-12-25', '2020-05-10'],
        'Department' : ['HR', 'Finance', 'Engineering', 'Engineering', 'HR', 'Engineering', 'Finance', 'HR'],
        'Salary' : [70000, 80000, 120000, 10000, 90000, 110000, 95000, 105000]
    }
)

dzisiejsza_data = pd.to_datetime('today') # ulepszyli i teraz pokazuje też czas
print('Dzisiaj jest', dzisiejsza_data)
print()
aktualny_czas = pd.Timestamp('now')
print('Teraz jest dokładnie', aktualny_czas)
print()

tylko_data = pd.to_datetime('now').normalize()
print('Tylko data:', tylko_data)
print()

print('Cały data frame:')
print(df)
print()
print('Typ danych:')
print(df.info())
print()

print('Nadpisanie formatu dla daty: "df["Hire Date"] = pd.to_datetime(df["Hire Date"])"')
df['Hire Date'] = pd.to_datetime(df['Hire Date'])
print(df.info())
print()

print('Dodanie nowych kolumn w opraciu o robicie dat na składowe:')
df['Year'] = df['Hire Date'].dt.year
df['Month'] = df['Hire Date'].dt.month
df['Day'] = df['Hire Date'].dt.day
df['Day of Week'] = df['Hire Date'].dt.dayofweek
df['Week of Year'] = df['Hire Date'].dt.isocalendar().week
print(df)
print()

print('Ile dni upłynęło od daty zatrudnienia:')
df['Days Since Hire'] = (pd.Timestamp('now') - df['Hire Date']).dt.days
df['Days passed'] = (pd.to_datetime('today') - df['Hire Date']).dt.days
print(df)
print()


print('Filtrowanie po dacie spełniającej kryterium:')
print(df['Hire Date'] > '2022-01-01')