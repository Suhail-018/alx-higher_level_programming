#!/usr/bin/python3
"""lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa"""


import sys

from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for recd in session.query(State).order_by(State.id):
        print(f"{recd.id}: {recd.name}")
        for city in recd.cities:
            print(f"{city.id}: {city.name}")
