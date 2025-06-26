import sqlite3
import pandas as pd

conn = sqlite3.connect('recap_db.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS DNI_TYGODNIA (
            PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_name TEXT NOT NULL)
""")

conn.commit()

print("Table meta-data")
cur.execute("PRAGMA table_info(DNI_TYGODNIA)")
for row in cur.fetchall():
    print(row)


cur.executemany("""
INSERT INTO DNI_TYGODNIA (Day_name) VALUES (?)
""", [
     ('Monday',), ('Tuesday',), ('Wednesday',), ('Thursday',), ('Friday',), ('Saturday',), ('Sunday',)
])

conn.commit()

table_as_is = cur.execute("""
SELECT * FROM DNI_TYGODNIA
""")


print()
print("Table content")
print(table_as_is.fetchall())

week_days_df = pd.read_sql("SELECT * FROM DNI_TYGODNIA", conn)
print()

print("Data frame taken from the table:")
print(week_days_df)