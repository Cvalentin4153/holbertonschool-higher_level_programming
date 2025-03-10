#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage:
    ./8-model_state_first.py
    <mysql_username> <mysql_password> <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Retrieves only the first state in ascending order by states.id.
- If the table states is empty, prints "Nothing".
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

    # Query the first State object by ascending id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Close the session
    session.close()
