import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Age" : ["25", "30", "thirty-five", "40", "Twenty-five"]
    }
)

print('Pierwsza wersja:')
print(df)
print()

# naprawa poprzez podmianę wartości a potem zmianę typu kolumny
print('Naprawa przez podmianę wartości a potem zmianę typu kolumny:')
df["Age"] = df["Age"].replace({"thirty-five" : 35, "Twenty-five" : 25})
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
print(df)
print()

# naprawa błędu walidacyjnego
print('Drugi data frame - z błędami logicznymi:')
df2 = pd.DataFrame(
    {
        "Name" : ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Age" : [25, 30, -35, 40, 125]
    }
)
print(df2)
print('Naprawa błędu walidacyjnego:')
df2.loc[(df2["Age"] < 0) | (df2["Age"] > 120), "Age"] = None
print(df2)
print()