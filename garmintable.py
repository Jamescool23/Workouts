import sqlite3 
     

db = sqlite3.connect("pfit.db")
dbcursor = db.cursor()
dbcursor.execute("DROP TABLE IF EXISTS pfit")

print("Database created and Successfully Connected to SQLite")

table =   """ Create Table Garmin (

    log_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    steps INT,
    step_goal INT,
    current_hr INT,
    avgResting_hr INT

);"""

dbcursor.execute(table)

print("Table is Ready")


db.close()












