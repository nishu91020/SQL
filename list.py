import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine=create_engine("C:\Windows\System32\cmd.exe\mydb.db")
mydb=scoped_session(sessionmaker(bind=engine))

def main():
    flights=mydb.execute("SELECT origin,destination,duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} takes {flight.duration} minutes")
if __name__=="__main__":
    main()
