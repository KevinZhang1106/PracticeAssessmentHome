#docstring - Kevin Zhang fighter jet database application
import sqlite3

#variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for fighter in results:
        print(fighter)
    db.close()

#main code
print_all_aircraft()