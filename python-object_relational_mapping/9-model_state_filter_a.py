#!/usr/bin/python3
"""
Lists all State objects that contain the letter
'a' from the database hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py
    <mysql_username> <mysql_password> <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Filters states where the name contains 'a'.
- Sorts results in ascending order by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects that have 'a' in their name
    states_with_a = (session.query(State)
                     .filter(State.name.like('%a%'))
                     .order_by(State.id)
                     .all())

    # Display each state in the format: "<id>: <name>"
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
