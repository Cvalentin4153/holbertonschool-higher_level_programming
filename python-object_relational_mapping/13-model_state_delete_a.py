#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./13-model_state_delete_a.py
    <mysql_username> <mysql_password> <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Deletes all states whose name contains 'a'.
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

    # Query all State objects whose name contains 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each matching state
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
