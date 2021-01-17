from django.conf.urls import url, include
from apps.user.views import *
urlpatterns = [
    url(r'^$', index, name='HomePage'),
    url(r'^SinUp$',SinUp , name='SinUp'),
]