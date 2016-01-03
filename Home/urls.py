from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.front, name='front'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog/(?P<slug>[^\.]+)/$', views.page, name='post')
    ]
