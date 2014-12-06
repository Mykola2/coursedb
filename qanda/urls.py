__author__ = 'Eric'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'details', 'qanda.views.details'),
                       url(r'add', 'qanda.views.add'),
                       url(r'delete_qst', 'qanda.views.delete_qst'),
                       url(r'delete_ans', 'qanda.views.delete_ans'),
                       url(r'search', 'qanda.views.search'),
                       url(r'register', 'qanda.views.register'),
                       url(r'login', 'qanda.views.login'),
                       url(r'logout', 'qanda.views.user_logout'),
                       url(r'unlike_qst', 'qanda.views.unlike_qst'),
                       url(r'like_qst', 'qanda.views.like_qst'),
                       url(r'unlike_ans', 'qanda.views.unlike_ans'),
                       url(r'like_ans', 'qanda.views.like_ans'),
                       url(r'chart1', 'qanda.views.chart1'),
                       url(r'', 'qanda.views.index')
                       )