#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa starting with 'N'.
Takes 3 arguments: username, password, and db_name.
Results are sorted in ascending order by states.id.
Uses MySQLdb to connect to a MySQL server running on localhost at port 3306.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line aguments.
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

# Connect to MySQL server.
conn = MySQLdb.connect(
    host = "localhost",
    username = username,
    password = password,
    db_name = db_name,
    port = 3306
)
# Create a cursor and execute query.
cursor = conn.cursor()
cursor.execute("SELECT * FROM states WHERE states.name like 'N%' ORDER BY states.id ASC")
# Fetch and display results.
rows = cursor.fetchall()
for row in rows:
    print(row)
# Close cursor and server connection.
cursor.close()
conn.close()