import MySQLdb
import sys



if __name__ == " __main__":
    
    with MySQLdb.connect(
    
            host="localhost",
            password="sys.argv[2]",
            database="sys.argv[3]",
            port="3306"
            ) as db:
 select_table = " SELECT * FROM states ORDER BY states.id AESC "

        with db.cursor() as cursor:
            cursor.execute(select_table)
            for row in cursor.fetchall():
                print(row)
