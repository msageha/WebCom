# coding: utf-8
from get_geo import tweet_geo
from get_lati_longi import from_place_to_lati_longi

print "地名を入力"

place = raw_input()

lat_lng = from_place_to_lati_longi(place)
lat, lng = lat_lng.values()

print "緯度:" + lat + ", 経度:" + lng

tweets = tweet_geo(lat, lng)

for tweet in tweets:
  print tweet.text

print len(tweets)