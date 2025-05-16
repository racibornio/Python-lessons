import pandas as pd

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('26__titanic.csv')
print(df.head(5).to_string())
print()