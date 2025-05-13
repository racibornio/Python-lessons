import pandas as pd

plik_do_korelacji_csv = pd.read_csv('do_korelacji.csv')
print('Plik do badania korelacji:')
print(plik_do_korelacji_csv)
print('Oblicz współczynnik korelacji:')
print(plik_do_korelacji_csv[["wiek", "wzrost"]].corr())
print()

print('Plik do badania korelacji 1:')
plik_do_korelacji_wprost_csv = pd.read_csv('korelacja_1.csv')
print(plik_do_korelacji_wprost_csv)
print('Oblicz współczynnik korelacji - jest 1:')
print(plik_do_korelacji_wprost_csv[["wiek", "wzrost"]].corr())
print()

print('Plik do badania korelacji -1:')
plik_do_korelacji_wprost_csv = pd.read_csv('korelacja_-1.csv')
print(plik_do_korelacji_wprost_csv)
print('Oblicz współczynnik korelacji - jest -1:')
print(plik_do_korelacji_wprost_csv[["wiek", "wzrost"]].corr())