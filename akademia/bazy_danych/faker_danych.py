import random
import sqlite3
import pandas as pd
from faker import Faker

fake = Faker()

employees = []
for i in range(1000):
    employees.append(
        {
            "id" : i + 1,
            "name" : fake.first_name(),
            "surname" : fake.last_name(),
            "age" : random.randint(20, 80) if random.random() > 0.1 else None,
            "salary" : random.randint(3000, 10000),
            "deparment" : random.choice(['IT', 'HR', 'Finance', 'Marketing'])
        }
    )


df = pd.DataFrame(employees)

with sqlite3.connect('learning_select.db') as conn:
        df.to_sql('employees', conn, if_exists='replace', index=False)



contracts = []
for i in range(700):
    contracts.append(
        {
            "employee_id" : i + 1,
            "type" : random.choice(['B2B', 'UoP']),
            "start" : fake.date_between(start_date='-5y', end_date='today'),
            "end" : fake.date_between(start_date='today', end_date='+5y')
        }
    )

    
for i in range(700, 1000):
    contracts.append(
        {
            "employee_id" : 1000 + i + 1,
            "type" : random.choice(['B2B', 'UoP']),
            "start" : fake.date_between(start_date='-5y', end_date='-1y'),
            "end" : fake.date_between(start_date='-1y', end_date='today')
        }
    )


df = pd.DataFrame(contracts)

with sqlite3.connect('learning_select.db') as conn:
     df.to_sql('contracts', conn, if_exists='replace', index=False)


with sqlite3.connect('learning_select.db') as conn:
     df = pd.read_sql('SELECT * FROM employees', conn)