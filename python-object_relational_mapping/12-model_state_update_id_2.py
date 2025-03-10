#!/usr/bin/python3
"""
Changes the name of the State object with id = 2
to "New Mexico" in the database hbtn_0e_6_usa.

Usage:
    ./12-model_state_update_id_2.py
    <mysql_username> <mysql_password> <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Updates the `name` of the State with `id=2` to "New Mexico".
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

    # Query for the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
