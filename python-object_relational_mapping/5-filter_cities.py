#!/usr/bin/python3
"""Takes the name of a state and lists all cities of that state
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

    cur.execute("""
                SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE %s
                ORDER BY cities.id;
                """,
                (SQL_search, )
                )

    rows = cur.fetchall()

    for idx, row in enumerate(rows):
        print(row[0], end="")
        if idx != len(rows) - 1:
            print(", ", end="")
    print()

    cur.close()
    db.close()
