from django.conf.urls import url
from django.contrib import admin

from twitter import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<username>\w+)', views.username),
    # url(r'^register/', views.register, name='register'), # don't think we need this
    url(r'^login/', views.login, name='login'),
    url(r'^$', views.index),
]

