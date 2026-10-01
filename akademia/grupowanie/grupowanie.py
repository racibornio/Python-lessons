import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
        "Age" : [25, 30, 35, 40, 25, 35, 30, 40],
        "City" : ["New York", "Los Angeles", "Los Angeles", "Houston", "New York", "Chicago", "Los Angeles", "Houston"],
        "Salary" : [70000, 80000, 120000, 100000, 90000, 110000, 95000, 105000],
        "Department" : ['HR', 'Finance', 'Engineering', 'Engineering', 'HR', 'Engineering', 'Finance', 'HR']
    }
)

print('Średnia wynagrodzenia wg grup miast:')
print(df.groupby('City', as_index=False)['Salary'].mean())
print()

print('Mediana wynagrodzenia dla grup miast:')
print(df.groupby('City', as_index=False)['Salary'].median())
print()

print('Ile jest rekordów w danej grupie:')
print(df.groupby('City', as_index=False)['Salary'].count())
print()

print('Oblicz kilka wielkości naraz:')
agg_df = df.groupby('City', as_index=False).agg({'Salary' : ['mean', 'median', 'count']})
print(agg_df)
print()

print('Kolumny:')
print(agg_df.columns)
print()

print('Zmiana nazw kolummn, żeby pozbyć się wielopoziomowego indeksu:')
agg_df.columns = ['City', 'Salary Mean', 'Salary Median', 'City Count']
print(agg_df)
print()

print('Min., max., średnia, mediana i odchylenie standardowe dla wieku i zarobków:')
print(
    df.groupby('City', as_index=False).agg(
        {
            'Age' : ['min', 'max', 'mean', 'median', 'std'],
            'Salary' : ['min', 'max', 'mean', 'median', 'std']
        }
    )
)
print()


print('Grupowanie po dwóch kolumnach:')
print(
    df.groupby(['City', 'Department'])[['Salary']].mean().reset_index()
)
print()


people_df = pd.DataFrame([
    { 'Name' : 'Alice', 'Age' : '25', 'City' : 'New York', 'Salary': 70000, 'Department' : 'HR'},
    { 'Name' : 'Alice', 'Age' : '26', 'City' : 'Los Angeles', 'Salary': 80000, 'Department' : 'HR'}
])
print('Grupowanie gdy duplikaty:')
print(
people_df.groupby('Name', as_index=False).agg({
    'Age' : 'first',
    'City' : 'last',
    'Salary' : 'mean'
})
)
print()



df_do_dat = pd.DataFrame(
    {
        'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
        'Hire Date' : ['2024-07-15', '2019-07-23', '2018-03-14', '2021-06-01', '2017-11-30', '2022-02-15', '2019-12-25', '2020-05-10'],
        'Department' : ['HR', 'Finance', 'Engineering', 'Engineering', 'HR', 'Engineering', 'Finance', 'HR'],
        'Salary' : [70000, 80000, 120000, 100000, 90000, 110000, 95000, 105000]
    }
)
print('Data frame przed konwersją dat:')
print(df_do_dat)
df_do_dat['Hire Date'] = pd.to_datetime(df_do_dat['Hire Date'])
print()
print('Data frame po konwersji dat:')
print(df_do_dat)
print()

print('Grupowanie po datach:')
print(
    df_do_dat.groupby(df_do_dat['Hire Date'].dt.year)['Salary'].mean().reset_index()
)
print()


print('Grupowanie po kolumnie dla obliczenia kilku agregacji:')
df_new = pd.DataFrame([
    {"name" : "Alice", "age" : 25, "city" : "Warsaw"},
    {"name" : "Bob", "age" : 30, "city" : "Krakow"},
    {"name" : "Charlie", "age" : 20, "city" : "Warsaw"},
    {"name" : "Ed", "age" : 21, "city" : "Warsaw"}
])
print(
    df_new.groupby('city')[["age"]].agg(['mean', 'median'])
)
print()


print('Grupowanie po roku wyłuskanym z kolumny daty:')
df_dat = pd.DataFrame([
    {"name" : "Alice", "date" : "2021-01-01"},
    {"name" : "Bob", "date" : "2021-02-01"},
    {"name" : "Charlie", "date" : "2022-01-01"}
])

df_dat['date'] = pd.to_datetime(df_dat['date'])
print(
    df_dat.groupby(df_dat['date'].dt.year).count()
)
print()