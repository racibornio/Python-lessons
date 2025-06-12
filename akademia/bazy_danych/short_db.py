import sqlite3
import pandas as pd

conn = sqlite3.connect('shortest_db.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS PERSONS (
    PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT,
    Last_name TEXT
)
""")

current_data_set = cur.execute("SELECT * FROM PERSONS")
print("Current db content - empty table created:")
print(current_data_set.fetchall())
print()
cur.execute("""
INSERT INTO PERSONS (First_name, Last_name) VALUES ('Andy', 'Adamovsky'),
            ('Browny', 'Bronovsky')
""")
conn.commit()

current_data_set = cur.execute("SELECT * FROM PERSONS")
print("Current db content - first three rows added:")
print(current_data_set.fetchall())
print()

#############################################################################
####################### DATA FRAME ADDED TO THE TABLE #######################
#############################################################################

df = pd.DataFrame({
    "PK_ID" : [4, 5, 6],
    "First_name" : ["Cezary", "Danny", "Eugene"],
    "Last_name" : ["Czary-mary", "Denny", "Eugeniczny"]
})
print("Data frame to be put into the table:")
print(df)
print()

############### THE LINE BELOW ADDS DATA FRAME TO THE TABLE ###############
df.to_sql("PERSONS", con=conn, if_exists="replace", index=False) # this will empty the table and start adding brand new rows
current_data_set = cur.execute("SELECT * FROM PERSONS")
print("Current db content - after adding extra rows from data frame:")
print(current_data_set.fetchall())
print()

# adding rows manually after transferring data frame to the table
cur.execute("""
INSERT INTO PERSONS (PK_ID, First_name, Last_name) VALUES (1, 'Andy', 'Adamovsky'),
            (2, 'Browny', 'Bronovsky')
""")
conn.commit()

current_data_set = cur.execute("SELECT * FROM PERSONS")
print("Current db content - rows added manually after transferring data frame to the table:")
print(current_data_set.fetchall())
print()

#############################################################################
######################## TABLE PUT IN THE DATA FRAME ########################
#############################################################################

############### THE LINE BELOW ADDS TABLE TO THE DATA FRAME ###############
df = pd.read_sql_query("SELECT * FROM PERSONS", conn)
print("Data frame after transferring the table:")
print(df)
print()







###################### IF NO CONNECTION ESTABLISHED ######################
# with sqlite3.connect("shortest_db.db") as conn:
#     instructions ...



# conn.close()