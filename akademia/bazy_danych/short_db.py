import sqlite3

conn = sqlite3.connect('shortest_db.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS PERSONS (
    PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT,
    Last_name TEXT
)
""")

cur.execute("""
INSERT INTO PERSONS (First_name, Last_name) VALUES ('Andy', 'Adamovsky'),
            ('Browny', 'Bronovsky')
""")
conn.commit()

current_data_set = cur.execute("SELECT * FROM PERSONS")
print("Current db content:")
print(current_data_set.fetchall())