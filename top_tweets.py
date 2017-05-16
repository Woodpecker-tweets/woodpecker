#!/usr/bin/python3
from twython import Twython
import sqlalchemy
import os
from models import tweeted

TWITTER_APP_KEY = os.getenv('TWITTER_APP_KEY')
TWITTER_APP_KEY_SECRET = os.getenv('TWITTER_APP_KEY_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN = '864521379676176385-iCxuc01ksOawg3yr2mYQwh8lcjVtGP9'
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
TWITTER_ACCESS_TOKEN_SECRET  = 'ZDEd6jhWCltxJN8gjga1j6fdkTFKsQR9y4gz56OndXQKO'
tclient = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def retweet(tclient, tid):
          """
          Retweets a given tweet, by tid.

          Returns false if the USER has already tweeted this before.
          Does not check if the SERVICE has already tweeted this before.

          Returns false if the user has already tweeted it, returns True
          if properly tweeted.
          """
          try:
                    tclient.retweet(id = tid)
          except Exception as err:
                    return(False)
          new_tweet = tweeted.Tweeted(tid)
          tweeted.save(new_tweet)


          return(True)

def top_100_tweets(hashtag, tclient, popular=True):
          """
          Grabs a list of the top 100 popular tweets, by hashtag.
          """
          if popular is True:
                    search = tclient.search(q=hashtag, result_type='popular', count=100)
          else:
                    search = tclient.search(q=hashtag, count=100)
          tweets = search['statuses']

          for tweet in tweets:
                    if not tweeted.check_if_tweeted(tweet['id']):
                              if retweet(tclient, tweet['id']) is True:
                                        return(True)
                    else:
                              pass
          return None

def do_retweet(hashtag):
          if top_100_tweets(hashtag, tclient) is True:
                    return("Tweeted properly.")
          else:
                    print("Failed to find a Tweet to tweet. Trying unpopular tweets...")
                    if (top_100_tweets(hashtag, tclient, False) is True):
                              return("Retweeted less popular tweet.")
                    else:
                              return("Failed to find any tweets to tweet.")
