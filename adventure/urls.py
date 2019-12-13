from django.conf.urls import url
from . import api, views

urlpatterns = [
    # url('', views.index, name='index'),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]