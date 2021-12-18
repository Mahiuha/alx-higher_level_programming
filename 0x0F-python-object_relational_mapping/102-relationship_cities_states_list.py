#!/usr/bin/python3
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys
"""
    Module that performs MySQL query through MySQLAlchemy.
"""


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])

    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for a_city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(a_city.id, a_city.name,
                  a_city.state.name))

    session.close()
