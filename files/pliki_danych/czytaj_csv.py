import pandas as pd
import os
print("Katalog roboczy:", os.getcwd())
os.chdir(os.path.dirname(__file__))

df = pd.read_csv('pierwszy_csv.csv')

print(df)

print()

x_df = pd.read_csv('x_sep.csv', sep='x')

print(x_df)

print()

space_sep = pd.read_csv('space_sep.csv', sep=' ')
print(space_sep)

print()

with open('zapis_z_ide.csv', 'w') as f:
    f.write("pierwszy,drugi,trzeci\n")
    f.write("1,11,111\n")
    f.write("2,22,\"2,222\"")

z_ide_df = pd.read_csv('zapis_z_ide.csv', sep=',', header=None, names=['1-ka', '2-ka', '3-ka'])

print(z_ide_df)

print()

samochody_df = pd.read_csv('samochody.csv', parse_dates=['data nabycia'])
print(samochody_df)
print()
print(samochody_df.dtypes)
print()
print(samochody_df.info)
print()
print(samochody_df.info())
print()