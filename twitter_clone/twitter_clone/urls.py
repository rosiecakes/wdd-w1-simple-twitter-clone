from django.conf.urls import url
from django.contrib import admin

from twitter import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.userlogin, name='login'),
    url(r'^logout$', views.userlogout, name='logout'),
    url(r'^(?P<username>\w+)$', views.tweets, name='tweets'),
    url(r'^(?P<tweet_id>\d+)/delete$', views.delete_tweet, name='delete_tweet')
]

