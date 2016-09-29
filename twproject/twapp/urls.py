# twapp/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [

    # Member URL View Routes
    url(r'^$', views.index, name='index'),
    url(r'^$', views.member_list, name="member_list"),
    url(r'^(?P<pk>\d+)/$', views.member_detail, name="member_detail"),

    # Tweet URL View Routes
    url(r'^$', views.tweet_list, name='tweet_list'),
    url(r'^(?P<id>\d+)/$', views.tweet_detail, name='tweet_detail'),
]
