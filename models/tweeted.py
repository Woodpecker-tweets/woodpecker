#!/usr/bin/python3
"""
Definition for tweeted tweets mapping
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Tweeted(Base):
                """
                Class for tweeted tweets
                """
                __tablename__ = 'tweeted'
                id = Column(String(60), primary_key=True)

                def __init__(self, tid):
                                self.id = int(tid)

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

uname = 'root'
upass = 'root'
dbname = 'woodpecker'
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(uname, upass, dbname))
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def save(new_tweet):
                """
                Saves a tweeted tweet to the tweeted table.
                """
                session.add(new_tweet)
                session.commit()

def all_retweeted():
                """
                Grabs all retweeted tweets (by the service)
                """
                return[instance.id for instance in session.query(Tweeted)]

def check_if_tweeted(tid):
                """
                Checks if we've already tweeted (by tweet id)
                """
                if tid in all_retweeted():
                                return True
                return False
