# from lecture3 selecting all the flights and printing them.

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:5504655@localhost/lecture4')
db = scoped_session(sessionmaker(bind=engine))

def main():
    selectAllFlight = db.execute('SELECT origin, destination, duration FROM flights')
    for flight in selectAllFlight:
        print(f'{flight.origin} to {flight.destination} in {flight.duration} minutes.')


if __name__ == '__main__':
    main()
