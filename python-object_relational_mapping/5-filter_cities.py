#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
This version is **safe from MySQL injections**.

Usage:
    ./5-filter_cities.py
    <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the database to connect to.
    state_name (str): The name of the state whose
    cities should be listed.

Functionality:
    - Connects to a MySQL database using MySQLdb.
    - Retrieves all cities belonging to the given state.
    - Sorts results in ascending order by `cities.id`.
    - Uses **only one `execute()` call**.
    - Prevents SQL injection using parameterized queries.

MySQL Server Requirements:
    - Must be running on localhost at port 3306.

Example Output:
    Dallas, Houston, Austin
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # ✅ Use parameterized query to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))  # Safe from SQL injection

    # Fetch and format results as a comma-separated list
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    # Close cursor and connection
    cursor.close()
    conn.close()
