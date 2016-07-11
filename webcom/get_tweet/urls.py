from django.conf.urls import url
from get_tweet import views

urlpatterns = [
  url(r'^v1/get_tweet/$', views.get_tweet, name='get_tweet'),
]