import pandas as pd
import sqlite3


#################################################################################
################################# CONFIGURATION #################################
#################################################################################

# establishing connection with the db
conn = sqlite3.connect('cars_db.db')
print("Connection established.")

# creating the querying object
cur = conn.cursor()
print("Querying object set up.")


#################################################################################
################################# CREATE TABLES #################################
#################################################################################

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


################################################################################
################################# WORK ON DATA #################################
################################################################################

# working on the table
print("Working with the tables")

# this will not display anything - will only perform query
cars_table_now = cur.execute("""
SELECT * FROM CARS
""")

print("Cursor object data:")
print(cars_table_now) # will display the cursor object data and not the result itself
print()
print("The data itself - all:")
print(cars_table_now.fetchall())
print()
print("One row of data:")
print(cars_table_now.fetchone())
print()
print("Given number of data:")
print(cars_table_now.fetchmany(6))
print()

# print("Table as data frame - pd.read_sql:")
# cars_table_now_df = pd.read_sql("SELECT * FROM CARS", conn)
# print(cars_table_now_df)
# print()

# print("Table as data frame - pd.read_sql_query:")
# cars_table_now_df = pd.read_sql_query("SELECT * FROM CARS", conn)
# print(cars_table_now_df)
# print()

# requires SQLAlchemy
# print("Table as data frame - pd.read_sql_table:")
# cars_table_now_df = pd.read_sql_table("CARS", conn)
# print(cars_table_now_df)
# print()


################################################################################
################################ INSERTING DATA ################################
################################################################################

# inserting data into the table
cur.execute("""
INSERT INTO CARS (Make, Model, Date_of_production) VALUES ('Audi', '3', 1999),
            ('Bentley', 'Azure', 2002),
            ('Chevrolet', 'Spark', 2008),
            ('Dodge', 'Caravan', 1998),
            ('Ford', 'Galaxy', 2009),
            ('GMC', 'AMX Pro Stocker', 2011),
            ('Hyundai', 'i30', 2010),
            ('Toyota', 'Auris', 2017)
""")
conn.commit()



# new read of all data
#################################################################################
################################# SELECTING DATA ################################
#################################################################################
print("New read of all data:")
cur.execute("SELECT * FROM CARS") # cursor object executes the query and...
all_data_now = cars_table_now.fetchall()
print(all_data_now) # ... it must be read by any of fetch
print()

# will take a number of rows - and leave cursor on the next position
print("Only given X of data:")
cur.execute("SELECT * FROM CARS") # reset cursor
only_first_row_now = cars_table_now.fetchmany(6)
print(only_first_row_now)
print()

# will take the very first row - and leave cursor on the next position
print("Only one row of data:")
cur.execute("SELECT * FROM CARS") # reset cursor
only_six_first_rows_now = cars_table_now.fetchone()
print(only_six_first_rows_now)
print()