import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    { "name" : "Alice", "age" : 21, "height" : 155 },
    { "name" : "Alice", "age" : 24, "height" : 160 },
    { "name" : "Bob", "age" : 30, "height" : 155 },
    { "name" : "Charlie", "age" : 20, "height" : 165 },
    { "name" : "Andrzej", "age" : 21, "height" : 192 },
    { "name" : "Adam", "age" : 31, "height" : 190 },
])

print('Czysty data frame:')
print(df)
print()

print('Sam wykres bez parametrów:')
print(df.plot())
print()

# histogram
#df.hist()
df["age"].hist(bins=3)
plt.show()

# wykres kolowy
df.plot(kind="pie", y="age", labels=df['name'], legend=True)
plt.show()

# wykres słupkowy
df.plot(kind="bar", x="name", y=["age", "height"])
plt.show()

# wykres punktowy
df.plot(kind="scatter", x="height", y="age")
plt.show()

# wykres pudełkowy
df.plot(kind="box")
plt.show()

# korelacja m-dzy zmiennymi
print('Korelacja:')
print(df[["age", "height"]].corr())
print()

# co potrafi metoda
print('Help do plota:')
print(help(df.plot))