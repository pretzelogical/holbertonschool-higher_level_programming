#!/usr/bin/python3
"""Gets all states from database hbtn_0e_0_usa
and prints it
Usage ./command username password database_name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    SQL_user = sys.argv[1]
    SQL_pass = sys.argv[2]
    SQL_db = sys.argv[3]

    # host="localhost" & port=3306 are default values
    db = MySQLdb.connect(user=SQL_user, passwd=SQL_pass, db=SQL_db)

    cur = db.cursor()

    cur.execute('SELECT id, name FROM states ORDER BY states.id ASC;')

    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
