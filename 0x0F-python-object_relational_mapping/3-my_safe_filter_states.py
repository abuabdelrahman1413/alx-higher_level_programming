#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    state_name = sys.argv[4]
    cur = mysql_db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE NAME  \
    LIKE %s",
        (sys.argv[4])
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    mysql_db.close()
