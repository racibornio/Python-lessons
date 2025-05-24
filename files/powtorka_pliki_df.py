from traceback import print_tb

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
print(f'Długość df (liczba wierszy) {df_length}')
print()


df_kolumny = len(df.columns)
print(f'Szerokość df (liczba kolumn): {df_kolumny}')
print()

df_size = df.size
print(f'Rozmiar/powierzchnia df (liczba komórek): {df_size}')
print()

df_shape = df.shape
print(f'Shape: {df_shape}')
df_shape_0 = df.shape[0]
print(f'Shape[0]: {df_shape_0}')
df_shape_1 = df.shape[1]
print(f'Shape[1]: {df_shape_1}')
print()

sum_inty = df['inty'].sum()
print(f'Sum inty: {sum_inty}')

count_inty = df['inty'].count()
print(f'Count inty: {count_inty}')
print()

sum_floaty = df['floaty'].sum()
print(f'Sum floaty: {sum_floaty}')

count_floaty = df['floaty'].count()
print(f'Count floaty: {count_floaty}')
print()

sum_stringi = df['stringi'].sum()
print(f'Sum stringi {sum_stringi}')

count_stringi = df['stringi'].count()
print(f'Count stringi: {count_stringi}')
print()

# sum_daty = df['daty'].sum()
# print(f'Sum daty: {sum_daty}')

count_daty = df['daty'].count() # zlicza wartości niepuste
print(f'Count daty: {count_daty}')
print()

null_inty = df['inty'].isnull() # zwraca obiekt Series typu bool
print(f'Nulle dla inty: {null_inty}')
suma_null_inty = df['inty'].isnull().sum()
print(f'Suma nulli dla inty: {suma_null_inty}')
print()

not_null_inty = df['inty'].notnull()
print(f'Not null dla inty: {not_null_inty}')
suma_not_null_inty = df['inty'].notnull().sum()
print(f'Suma not null dla inty: {suma_not_null_inty}')
print()

for column in df.columns:
    column_type = df[column].dtype
    if column_type != 'object':
        column_sum = df[column].sum()
        print(f'Suma kolumny {column} wynosi: {column_sum}.')


print()
for column in df.columns:
    column_count = df[column].count()
    null_count = df[column].isnull().sum()
    not_null_count = df[column].notnull().sum()
    print(f'Kolumna {column} zawiera {column_count} wartości niepustych i {null_count} null i {not_null_count} not null.')