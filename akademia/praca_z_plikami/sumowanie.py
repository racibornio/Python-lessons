import pandas as pd

file_to_analyze = pd.read_csv('do_scalania_1.csv')
print('Plik z csv:')
print(file_to_analyze)
print()

df = pd.DataFrame(file_to_analyze)

# nazwa każdej kolumny i suma dla niej - każda w osbnym wierszu
print('Suma dla każdej kolumny numerycznej:')
print(df.sum(numeric_only=True))
print()

print('Dodanie kolumny sumującej każdy wiersz po numerycznych:')
df2 = df.copy()
df2["Total"] = df2.sum(axis=1, numeric_only=True)
print(df2)
print()

print('Jedna suma:')
print(df.sum(numeric_only=True).sum())
print()