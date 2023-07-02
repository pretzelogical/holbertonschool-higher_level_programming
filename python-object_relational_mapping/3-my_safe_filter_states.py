#!/usr/bin/python3
"""Gets all states from database hbtn_0e_0_usa
that match the state name arg (safe version)
Usage: ./command username password database_name state_name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    SQL_user = sys.argv[1]
    SQL_pass = sys.argv[2]
    SQL_db = sys.argv[3]
    SQL_search = sys.argv[4]

    # host="localhost" & port=3306 are default values
    db = MySQLdb.connect(user=SQL_user, passwd=SQL_pass, db=SQL_db)
    cur = db.cursor()

    cur.execute("""SELECT id, name
                FROM states
                WHERE name LIKE %s
                ORDER BY id ASC;""",
                (SQL_search, ))

    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
