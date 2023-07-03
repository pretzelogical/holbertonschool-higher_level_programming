#!/usr/bin/python3
""" Lists the id of a State object based on the name passed """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State)
             .filter(State.name == sys.argv[4])
             .order_by(State.id)
             .all())

    if state:
        print(state.id)  # type: ignore
    else:
        print("Not Found")

    session.close()
