# coding: utf-8
from googlemaps import Client
import json

api_key_json_path = './api_key.json'
with open(api_key_json_path, 'r') as f:
  API_KEY = json.load(f)['googleMap']

def from_place_to_lati_longi(place):
  gmaps = Client(API_KEY)
  address = place
  lat_lng = gmaps.geocode(address)[0][u'geometry'][u'location']
  return lat_lng

if __name__ == "__main__":
  place = input()
  print (from_place_to_lati_longi(place))
