from django.conf.urls import url, include
from apps.post.views import index
urlpatterns = [
    url(r'^$', index, name='Index'),
]