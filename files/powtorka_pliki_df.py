import pandas as pd

df = pd.read_csv('metody_df.csv')
print(df)
print()

print('Pokaż kolumny:')
print(df.columns)
print()
print('Iterowanie po kolumnach:')
for kolumna in df:
    print(kolumna)


print()
print('Pokaż typy danych:')
print(df.dtypes)
print()

lista_kolumn = df.columns.to_list()
print('Lista kolumn jako zmienna:')
print(lista_kolumn)
print()

print('Iterowanie po liście kolumn:')
for i in lista_kolumn:
    print(i)


print()
print('Typ listy:')
print(type(lista_kolumn))

print()
df_length = len(df)
print(f'Length data frame {df_length}')
print()


df_kolumny = len(df.columns)
print(f'Kolumny: {df_kolumny}')
print()

df_size = df.size
print(f'Size df: {df_size}')
print()

df_shape = df.shape
print(f'Shape: {df_shape}')
df_shape_0 = df.shape[0]
print(f'Shape[0]: {df_shape_0}')
df_shape_1 = df.shape[1]
print(f'Shape[1]: {df_shape_1}')

