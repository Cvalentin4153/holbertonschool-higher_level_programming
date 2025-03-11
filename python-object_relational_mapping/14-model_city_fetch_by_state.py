#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Usage:
  ./14-model_city_fetch_by_state.py
  <mysql_username> <mysql_password> <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by cities.id.
- The format is: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all City objects, joined with their corresponding State
    # Order by city.id ascending
    query = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
    )

    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
