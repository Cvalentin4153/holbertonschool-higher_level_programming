#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.

Usage:
    ./4-cities_by_state.py
    <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the database to connect to.

Functionality:
    - Connects to a MySQL database using MySQLdb.
    - Retrieves all cities, displaying their IDs, names,
      and corresponding states.
    - Uses only one `execute()` call.
    - Sorts results in ascending order by `cities.id`.

MySQL Server Requirements:
    - Must be running on localhost at port 3306.

Example Output:
    (1, 'San Francisco', 'California')
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Use only one `execute()` call to join cities with states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
