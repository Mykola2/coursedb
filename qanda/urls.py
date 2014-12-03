__author__ = 'Eric'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'details', 'qanda.views.details'),
                       url(r'add', 'qanda.views.add'),
                       url(r'search', 'qanda.views.search'),
                       url(r'register', 'qanda.views.register'),
                       url(r'login', 'qanda.views.login'),
                       url(r'logout', 'qanda.views.user_logout'),
                       url(r'restricted', 'qanda.views.restricted'),
                       url(r'', 'qanda.views.index')
                       )