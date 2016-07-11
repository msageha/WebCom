# coding: utf-8
import sys
import twitter


CONSUMER_KEY = "GG96kwKXN2f6k5eS7El1eWyyF"
CONSUMER_SECRET = "XDNMc0XIlZAcuxDNyPfB5N32xrizNEgiUgYrdEhPYNcFDTj2sz"
ACCESS_TOKEN_KEY = "2506162753-F7HKMVe4nP32R4qDYydN3tDiDBxXLPPlVuQPk0n"
ACCESS_TOKEN_SECRET = "tlJpcDn4UNiciFsE6XSeQYKR1PKhQMwip6r6UhJ1pUFPL"

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)



def tweet_geo(latitude, longitude):
  tweets_get_geo = []
  # s = set()
  i = 0
  tweets = api.GetSearch(geocode=[latitude, longitude, u"1km"],count=200) #仙台
  for k in range(0,1):
    for tweet in tweets:
        if tweet.geo != None and i <= 10: #一応geoタグが，違うものは省く
          tweets_get_geo.append(tweet)
          i += 1

    maxid = tweets[len(tweets)-1].id
    tweets = api.GetSearch(geocode=[latitude, longitude, u"1km"],count=200, max_id=maxid)
    
  for tweet in tweets:
    if tweet.geo != None and i <= 10: #一応geoタグが，違うものは省く
      tweets_get_geo.append(tweet)

  # print len(tweets_get_geo)
  # print len(s)
  return tweets_get_geo

if __name__ == "__main__":
  tweet_geo(0,0)
