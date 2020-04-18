import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine("sqlite:///C:\\Users\\sysadmin\\Desktop\\Nishu\\sqlite3\\SQL\\mydb.db")
mydb=scoped_session(sessionmaker(bind=engine))

def main():
    f= open("flight.csv")
    reader =  csv .reader(f)
    for origin,destination,duration in reader:
        mydb.execute("insert into flights(origin,destination,duration) values (:origin,:destination,:duration)",
                     {"origin":origin , "destination":destination , "duration":duration})
        print(f"{origin} to {destination} takes {duration} minutes")
    mydb.commit()

if __name__=="__main__":
    main()