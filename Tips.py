import sqlite3 
     

db = sqlite3.connect("pfit.db")
dbcursor = db.cursor()
dbcursor.execute("DROP TABLE IF EXISTS pfit")

print("Database created and Successfully Connected to SQLite")

table =   """ Create Table Tips (

    tip_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    exercise_tip

);"""

dbcursor.execute(table)

print("Table is Ready")


db.close()