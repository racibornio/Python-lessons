import pandas as pd
import sqlite3

# establishing connection with the db
conn = sqlite3.connect('cars_db.db')
print("Connection established.")

# creating the querying object
cur = conn.cursor()
print("Querying object set up.")


# creating the first table
cur.execute("""
CREATE TABLE IF NOT EXISTS CARS (
    PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Make TEXT,
    Model TEXT,
    Date_of_production DATE
)
""")

# displaying the table metadata - SQLite-style
print('Table "cars" created - PRAGMA:')
print()
cur.execute("PRAGMA table_info(CARS)")
for row in cur.fetchall():
    print(row)


# displaying the table metadata - Pandas-style
print()
print("Pandas-style for the table metadata:")
cars_df = pd.read_sql_query("PRAGMA table_info(CARS)", conn)
print(cars_df)
print()



# creating the second table
cur.execute("""
CREATE TABLE IF NOT EXISTS PERSONS (
    PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Frist_name TEXT,
    Middle_name TEXT,
    Last_name TEXT,
    Identity_card TEXT
)
""")

# displaying the table metadata - SQLite-style
print('Table "persons" created - PRAGMA:')
print()
cur.execute("PRAGMA table_info(PERSONS)")
for row in cur.fetchall():
    print(row)


# displaying the table metadata - Pandas-style
print()
print("Pandas-style for the table metadata:")
persons_df = pd.read_sql_query("PRAGMA table_info(PERSONS)", conn)
print(persons_df)
print()