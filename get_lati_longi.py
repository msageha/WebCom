# coding: utf-8
from googlemaps import Client

API_KEY = "AIzaSyBBLfpk0-ZwbmcFf7grnMArYGjSb86qIlA"

def from_place_to_lati_longi(place):
  gmaps = Client(API_KEY)
  address = place
  lat_lng = gmaps.geocode(address)[0][u'geometry'][u'location']
  return lat_lng

if __name__ == "__main__":
  place = raw_input()
  print from_place_to_lati_longi(place)
