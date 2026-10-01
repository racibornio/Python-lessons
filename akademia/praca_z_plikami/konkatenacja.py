import pandas as pd

lista_concat_1_df = pd.read_csv('do_konkatenacji_1_2.csv')
print('Pierwszy plik:')
print(lista_concat_1_df)
print()

lista_concat_2_df = pd.read_csv('do_konkatenacji_2_2.csv')
print('Drugi plik:')
print(lista_concat_2_df)
print()

print('Połączone:')
poloczone_df = pd.concat([lista_concat_1_df, lista_concat_2_df], ignore_index=True)
print(poloczone_df)
print()