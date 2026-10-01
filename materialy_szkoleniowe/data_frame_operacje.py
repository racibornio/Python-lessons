import pandas as pd

df = pd.DataFrame(
    [
        {"name" : "Adam", "age" : 34, "weight" : 80, "height" : 183},
        {"name" : "Bartłomiej", "age" : 43, "weight" : 89, "height" : 179},
        {"name" : "Dominika", "age" : 51, "weight" : 66, "height" : 164},
        {"name" : "Tomasz", "age" : 29, "weight" : 48, "height" : 159}
    ]
)

print("Zastany data frame:")
print(df)