# coding: utf-8
import sys
import twitter
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


def tweet_get_info(twitter_id):

  CONSUMER_KEY = "GG96kwKXN2f6k5eS7El1eWyyF"
  CONSUMER_SECRET = "XDNMc0XIlZAcuxDNyPfB5N32xrizNEgiUgYrdEhPYNcFDTj2sz"
  ACCESS_TOKEN_KEY = "2506162753-F7HKMVe4nP32R4qDYydN3tDiDBxXLPPlVuQPk0n"
  ACCESS_TOKEN_SECRET = "tlJpcDn4UNiciFsE6XSeQYKR1PKhQMwip6r6UhJ1pUFPL"

  api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

  
  tweets = api.GetUserTimeline(twitter_id,count=200)

  maxid = 0
  words = set()
  for k in range(0,20):
    for tweet in tweets:
        # print tweet.text.rfind(u"#用語")
        if tweet.geo != None:
          print tweet.geo

    maxid = tweets[len(tweets)-1].id
    tweets = api.GetUserTimeline(twitter_id,count=200, max_id=maxid)
  
  print "maxid = " + str(maxid)

class tweet_search(StreamListener):
  def on_data(self, data):
    if data.startswith("{"):
      type(data)
 
  def on_error(self, status):
    print status

geocode=[37.781157, -122.398720, "1mi"]
def tweeet_geo(latitude, longitude):
  tweets = api.GetSearch(geocode=[38.295728, 140.856325, "1km"],count=200, max_id=maxid) #仙台



if __name__ == "__main__":
  twitter_id = raw_input()

  a = tweet_get_info(twitter_id)
  l = tweet_search()
  a = Stream(auth, l).filter(locations = [122.87, 24.84, 153.01, 46.80])