#!/usr/bin/python3
"""
Lists all states from the database
hbtn_0e_0_usa that match a given name.
This version is **safe from MySQL injections**.

Usage:
    ./3-my_safe_filter_states.py
    <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the database to connect to.
    state_name (str): The name of the state to search for.

Functionality:
    - Connects to a MySQL database using MySQLdb.
    - Retrieves all states where the name matches the user input.
    - Sorts results in ascending order by `id`.
    - Prevents SQL injection using parameterized queries.

MySQL Server Requirements:
    - Must be running on localhost at port 3306.

Example Output:
    (2, 'Arizona')
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
        SELECT * FROM states
        WHERE BINARY name = %s
        ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))  # 👈 Safe from SQL injection

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
