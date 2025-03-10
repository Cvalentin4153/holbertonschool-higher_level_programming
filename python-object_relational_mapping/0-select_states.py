#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print each row
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
