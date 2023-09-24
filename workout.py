import sqlite3 
     

db = sqlite3.connect("pfit.db")
dbcursor = db.cursor()
dbcursor.execute("DROP TABLE IF EXISTS pfit")

print("Database created and Successfully Connected to SQLite")


table = """ CREATE TABLE Workout (
        workout_id INT PRIMARY KEY,
        user_id INT,
        workout_date DATE,
        exercise VARCHAR(255),
        sets INT,
        reps INT,
        weight DECIMAL(10, 2),
        duration_minutes INT
);"""

dbcursor.execute(table)

print("Table is Ready")


db.close()

