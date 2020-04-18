import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine("sqlite:///C:\\Users\\sysadmin\\Desktop\\Nishu\\sqlite3\\SQL\\mydb.db")
mydb=scoped_session(sessionmaker(bind=engine))

def main():
    flights=mydb.execute("select id ,origin,destination,duration from flights").fetchall()
    for flight in flights:
        print(f"flight {flight.id}:{flight.origin} to {flight.destination},{flight.duration}")
    flight_id=int(input("enter flight id:"))
    flight=mydb.execute("select origin,destination,duration from flights where id=:id",{"id":flight_id}).fetchone()
    if flight is None:
        print("error:no such flight")
        return
    passengers=mydb.execute("select name from passangers where flight_id=:flight_id",
                            {"flight_id":flight_id}).fetchall()
    print("\n passangers:")
    for passanger in passangers:
        print(passanger.name)
    if len(passangers)==0:
        print("no passangers")
