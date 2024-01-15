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

    select_table = """SELECT * FROM states
                  WHERE states.name = %s
                  ORDER BY id ASC"""
    cursor = db.cursor()
    cursor.execute(select_table, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
