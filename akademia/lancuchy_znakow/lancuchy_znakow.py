import random

import pandas as pd

df = pd.DataFrame({
    "Name" : ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Wilson", "Emma Davis"],
    "Email" : ["alice@example.com", "bob@gmail.com", "charlie@example.com", "david@wp.pl", "emma@example.com"],
    "City" : ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
})

print('Wyświetl data frame:')
print(df)
print()

print('Rozdziel kolumnę na dwie:')
df[["First Name", "Last Name"]] = df["Name"].str.split(' ', expand=True)
print(df)
print()

print('Czy adresy dana fraza w kolumnie? Tu "gmail" jako adres e-mail:')
df["isGmail?"] = df["Email"].str.contains("gmail")
print(df)
print()


print('Czy to działa:')
print(df["Email"])
print('Elementów jest', len(df["Email"]))
print('Element drugi to', df["Email"][1])
print()

print('Zastąp/anonimizuj dane:')
df_copy = df.copy()

alfabet = list('qwertyuiopasdfghjklzxcvbnm')
for i in range(len(df_copy)):
    wylosowana_litera = random.choice(alfabet)
    df_copy.at[i, 'Email'] = df_copy.at[i, 'Email'].replace('@', wylosowana_litera, 1)


print(df_copy)
print()


print('Wyłuskaj imiona i nazwiska z adresów E-mail')
df['Username'] = df['Email'].str.split('@').str[0]
print(df)

print('Łączenie stringów - kto skąd:')
df['Username and City'] = df['Username'] + ' from ' + df['City']
print(df)

print('Dodaj kolumnę pokazującą ilość znaków innej kolumny:')
df['Entry length'] = df['Username'].str.len()
print(df)