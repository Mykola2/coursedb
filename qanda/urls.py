__author__ = 'Eric'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'add', 'qanda.views.add'),
                       url(r'', 'qanda.views.index')
                       )