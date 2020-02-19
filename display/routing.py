# display/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/display/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/display/$', consumers.DisplayConsumer),
]