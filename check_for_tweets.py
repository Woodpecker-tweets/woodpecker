#!/usr/bin/python3
"""
Definition for tweeted tweets mapping
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
                """
                Class for tweeted tweets
                """
                __tablename__ = 'users'
                user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
                user_name = Column(String(60), nullable=False)
                oauth_token = Column(String(100))
                oauth_token_secret = Column(String(100))
                active = Column(Integer, nullable=False)
                hashtag = Column(String(200))
                tweet_time = Column(Integer)
                counter = Column(Integer, nullable=False)

                def __init__(self, user_name, tweet_time):
                    self.user_name = user_name
                    self.oauth_token = None
                    self.oauth_secret = None
                    self.active = True
                    self.hashtag = None
                    self.tweet_time = tweet_time
                    self.counter = 0

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
                uname = 'root'
                upass = 'root'
                dbname = 'woodpecker'
                engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                       .format(uname, upass, dbname))
                Base.metadata.create_all(engine)

                Session = sessionmaker()
                Session.configure(bind=engine)
                session = Session()


                for user in session.query(User).filter(User.active == 1):
                                if user.hashtag is not None and user.oauth_token is not None:
                                                user.counter += 1
                                                print(user.counter)
                                                if user.counter >= user.tweet_time:
                                                                user.counter = 0
                                                                print("Tweeting")
                session.commit()
