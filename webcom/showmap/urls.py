from django.conf.urls import url
from showmap import views

urlpatterns = [
  url(r'', views.show_maps_html, name='show_maps_html'),
  url(r'^v1/showmap/show_maps.html', views.show_maps_html, name='show_maps_html'),
  url(r'^v1/showmap/show_maps.css', views.show_maps_css, name='show_maps_css'),
  url(r'^v1/showmap/show_maps.js', views.show_maps_js, name='show_maps_js'),
]
