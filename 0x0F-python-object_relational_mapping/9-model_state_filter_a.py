#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State objects containing the letter 'a'
    for state_a in session.query(State).order_by(State.id)\
            .filter(State.name.like("%a%")):
        print(f"{state_a.id}: {state_a.name}")
