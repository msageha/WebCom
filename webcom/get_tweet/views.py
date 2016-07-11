# coding: utf-8
from django.shortcuts import render
import json
from django.http import HttpResponse
from get_geo import tweet_geo
from get_lati_longi import from_place_to_lati_longi

# Create your views here.

def get_tweet(request):

  place = request.GET["place"]

  lat_lng = from_place_to_lati_longi(place)
  lat, lng = lat_lng.values()

  print "緯度:" + str(lat) + ", 経度:" + str(lng)
  tweets = tweet_geo(lat, lng)

  i = 0
  tweets_dic = {}
  for tweet in tweets:
    tweet_dic = {"text": tweet.text, "geo": tweet.geo}
    tweets_dic[str(i)] = tweet_dic
    i += 1
    # print tweet.text

  print len(tweets)
  print request.GET
  return json_response(request, tweets_dic)

def json_response(request, data, status=None):
  json_str = json.dumps(data, ensure_ascii=False, indent=2)
  callback = request.GET.get('callback')
  if not callback:
    callback = request.POST.get('callback')  # POSTでJSONPの場合
  if callback:
    json_str = "%s(%s)" % (callback, json_str)
    response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
  else:
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
  return response