from django.conf.urls import url
from . import views
from .forms import LoginForm

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # Signup
    url(r'^signup/$', views.signup_form, name="signup_form"),

    # Login
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LoginForm}, name='login'),

    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', views.index, name='index'),

    # Posting
    url(r'^post/$', views.posting_form, name='posting_form'),

    # Member URL View Routes
    url(r'^members/$', views.member_list, name="member_list"),
    url(r'^member_tweets/([0-9]+)/$', views.member_tweets, name="member_tweets"),

    # Tweet URL View Routes

    url(r'^tweets/$', views.tweet_list, name='tweet_list'),
    #url(r'^(?P<id>\d+)/$', views.tweet_detail, name='tweet_detail'),

    

]