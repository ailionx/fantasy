from django.conf.urls import url
from . import views

app_name = 'listings'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^region/(?P<pk>[0-9]+)/$', views.Region.as_view(), name='region'),
]
