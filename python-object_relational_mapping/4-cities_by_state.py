#!/usr/bin/python3
"""Gets all cities and states and prints a joined table
Usage: ./command username password database_name
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

    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """
                )

    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
