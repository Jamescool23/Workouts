import sqlite3 
     

db = sqlite3.connect("pfit.db")
dbcursor = db.cursor()
dbcursor.execute("DROP TABLE IF EXISTS pfit")

print("Database created and Successfully Connected to SQLite")


table = """ CREATE TABLE WorkoutList (
        exercise_id INT PRIMARY KEY,
        exercise_name TEXT, 
        muscle_group TEXT 
);"""

dbcursor.execute(table)

print("Table is Ready")


db.close()