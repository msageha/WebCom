# coding: utf-8
import sys
import json
from requests_oauthlib import OAuth1Session

url = "https://api.twitter.com/1.1/search/tweets.json"

api_key_json_path = './api_key.json'
with open(api_key_json_path, 'r') as f:
  twitter_json = json.load(f)['twitter']
  CONSUMER_KEY = twitter_json['CONSUMER_KEY']
  CONSUMER_SECRET = twitter_json['CONSUMER_SECRET']
  ACCESS_TOKEN_KEY = twitter_json['ACCESS_TOKEN_KEY']
  ACCESS_TOKEN_SECRET = twitter_json['ACCESS_TOKEN_SECRET']

twitter = OAuth1Session(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY,
                  ACCESS_TOKEN_SECRET)

def tweet_geo(latitude, longitude):
  tweets_get_geo = []
  # s = set()
  i = 0
  params = {'geocode': f'{latitude},{longitude},1km', 'count':20}
  req = twitter.get(url, params= params) #仙台
  if req.status_code == 200:
    tweets = json.loads(req.text)
    for tweet in tweets['statuses']:
      if tweet['geo'] != None and i <= 10: #一応geoタグが，違うものは省く
        tweets_get_geo.append(tweet)
        i += 1

  # maxid = tweets[len(tweets)-1].id
  # tweets = api.GetSearch(geocode=[latitude, longitude, u"1km"],count=200, max_id=maxid)

  # for tweet in tweets:
  #   if tweet.geo != None and i <= 10: #一応geoタグが，違うものは省く
  #     tweets_get_geo.append(tweet)

  # print len(tweets_get_geo)
  # print len(s)
  return tweets_get_geo

if __name__ == "__main__":
  tweet_geo(38.268215, 140.8693558)
