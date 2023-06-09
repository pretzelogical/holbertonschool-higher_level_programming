#!/usr/bin/python3
""" Updates any state where id=2 so name='New Mexico' """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State)
              .filter(State.id == 2)
              .all())

    for state in states:
        state.name = "New Mexico"  # type: ignore
    session.commit()

    session.close()
