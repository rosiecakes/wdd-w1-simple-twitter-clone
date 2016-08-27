from django.conf.urls import url
from django.contrib import admin

from twitter import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_login$', views.user-login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)$', views.username, name='username-hp'),
    # url(r'^register/', views.register, name='register'), # don't think we need this
]

