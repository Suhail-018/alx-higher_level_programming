#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        password=password,
        database=database,
        port=3306
    )

    select_table = """SELECT cities.name FROM states
                  JOIN  cities ON states.id = cities.state_id
                  WHERE states.name = %s
                   """
    cursor = db.cursor()
    cursor.execute(select_table, (sys.argv[4],))
    result = []
    for row in cursor.fetchall():
        result += row

    print(', '.join(result), end="")
    print()

    cursor.close()
    db.close()
