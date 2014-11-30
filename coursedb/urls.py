from django.conf.urls import patterns, include, url
from django.contrib import admin
import qanda.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coursedb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('' , include(qanda.urls))
)
