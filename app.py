#docstring - Kevin Zhang fighter jet database application
import sqlite3

#variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY aircraft DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

def print_all_aircraft_speed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

def print_all_aircraft_max_g():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY max_g DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

def print_all_aircraft_climbrate():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY climbrate"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

def print_all_aircraft_range():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY range DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

def print_all_aircraft_payload():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY payload DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("name                          speed(km/h)     max_g       climb(m/s)  range(km)       payload(kg)")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<16}{fighter[3]:<12}{fighter[4]:<12}{fighter[5]:<16}{fighter[6]:<12}")
    db.close()

#main code
while True:
    user_input = input(
    """
    What would you like to do.
    1. Print all aircraft
    2. Print all aircraft sorted by speed(km/h)
    3. Print all aircraft sorted by max g force
    4. Print all aircraft sorted by climbrate(m/s)
    5. Print all aircraft sorted by range(km)
    6. Print all aircraft sorted by payload(kg)
    7. Exit
    """)
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_speed()
    elif user_input == "3":
        print_all_aircraft_max_g()
    elif user_input == "4":
        print_all_aircraft_climbrate()
    elif user_input == "5":
        print_all_aircraft_range()
    elif user_input == "6":
        print_all_aircraft_payload()
    elif user_input == "7":
        break
    else:
        print("That was not an option")

    