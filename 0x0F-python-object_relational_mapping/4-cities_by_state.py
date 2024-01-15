#!/usr/bin/python3
"""list all states from the database hbtn_0e_0_usa"""

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

    select_table = """SELECT cities.id, cities.name, states.name
                  FROM states
                  JOIN  cities ON states.id = cities.state_id
                  ORDER BY cities.id ASC"""
    cursor = db.cursor()
    cursor.execute(select_table)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
