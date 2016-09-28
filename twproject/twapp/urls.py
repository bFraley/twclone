# twapp/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^member-list/$', views.MemberList.as_view(), name="member_list"),
    url(r'^(?P<pk>\d+)/member-detail/$', views.MemberDetail.as_view(), name="member_detail"),

]
