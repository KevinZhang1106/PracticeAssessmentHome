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
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

#main code
print_all_aircraft()