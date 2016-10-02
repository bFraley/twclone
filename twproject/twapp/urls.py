from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # Signup
    url(r'^signup/$', views.signup_form, name="signup_form"),

    # Login
    url(r'^login/$', views.login_form, name="login_form"),

    # Posting
    url(r'^post/$', views.posting_form, name='posting_form'),

    # Member URL View Routes
    url(r'^members/$', views.member_list, name="member_list"),
    #url(r'^members/(?P<id>\d+)/$', views.member_detail, name="member_detail"),

    # Tweet URL View Routes

    url(r'^tweets/$', views.tweet_list, name='tweet_list'),
    #url(r'^(?P<id>\d+)/$', views.tweet_detail, name='tweet_detail'),
]