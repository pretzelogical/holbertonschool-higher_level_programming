#!/usr/bin/python3
""" Adds the state object Louisiana to the database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_la = State(name="Louisiana")
    session.add(state_la)
    session.commit()
    print(state_la.id)

    session.close()
