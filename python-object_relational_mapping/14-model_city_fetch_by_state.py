#!/usr/bin/python3
""" Prints city objects from hbtn_0e_14_usa """
import sys
from model_state import Base, State
from model_city import City  # type: ignore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(State, City)
             .filter(State.id == City.state_id)
             .order_by(City.id)
             .all())

    for state, city in query:
        print(f"{state.name}: {city.id} {city.name}")

    session.close()
