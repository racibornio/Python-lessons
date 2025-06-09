import pandas as pd
import sqlite3

conn = sqlite3.connect("baza_1.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    wiek INTEGER NOT NULL
            )
""")

cur.execute("""
INSERT INTO clients (imie, nazwisko, wiek) VALUES ('Patryk', 'Ostrowski', 43)
""")

df = pd.DataFrame({
    "imie" : ["Andrzej", "Bronek", "Czesiek"],
    "nazwisko" : ["Andrzejczak", "Bronciarz", "Czechowski"],
    "wiek" : [5, 10, 15]
})

df.to_sql("clients", con=conn, if_exists="append", index=False)

cur.execute("SELECT * FROM clients")
cur.fetchall()

df = pd.read_sql_query("SELECT * FROM clients", conn)
print("Data frame po wypełnieniu danymi w tabeli:")
print(df)
print()

with sqlite3.connect("baza_1.db") as conn:
    df = pd.read_sql_query("SELECT * FROM clients WHERE nazwisko = 'Ostrowski'", conn)
    print("Tylko jedno nazwisko:")
    print(df)

conn.close()