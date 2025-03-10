#!/usr/bin/python3
"""
Prints the State object's id with the given name
from the database hbtn_0e_6_usa.
(SQL injection free)

Usage:
    ./10-model_state_my_get.py
    <mysql_username> <mysql_password> <database_name> <state_name>

- Connects to a MySQL server running on localhost at port 3306.
- If the state name is found, prints its id.
- Otherwise, prints "Not found".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_state = sys.argv[4]

    # Create an SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object with the name = searched_state
    # Using .filter() with Python variables is safe from SQL injection
    # in SQLAlchemy
    found_state = (
        session.query(State)
        .filter(State.name == searched_state)
        .first()
    )

    # Print the result
    if found_state:
        print(found_state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
