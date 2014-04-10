from django.conf.urls import patterns, url

from summoners import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^info$', views.info, name='info'),
)
