import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
        "Age" : [25, 30, 35, 40, 25, 35, 30, 40],
        "City" : ["New York", "Los Angeles", "Los Angeles", "Houston", "New York", "Chicago", "Los Angeles", "Houston"],
        "Salary" : [70000, 80000, 120000, 100000, 90000, 110000, 95000, 105000],
        "Department" : ['HR', 'Finance', 'Engineering', 'Engineering', 'HR', 'Engineering', 'Finance', 'HR']
    }
)

print(df.groupby('City', as_index=False)['Salary'].mean())