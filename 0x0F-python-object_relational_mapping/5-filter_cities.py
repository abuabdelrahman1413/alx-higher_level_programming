#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_0_usa where the state name matches the provided argument """
import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor object
    cur = db.cursor()
    
    # Execute the query
    cur.execute("""SELECT cities.name FROM cities INNER JOIN\
                states ON cities.state_id = states.id\
                WHERE states.name = %s""", (sys.argv[4],))
    
    # Fetch all the results
    rows = cur.fetchall()
    
    # Print the results
    print(", ".join([row[0] for row in rows]))
    
    # Close the cursor and connection
    cur.close()
    db.close()
