from django.conf.urls import patterns, include, url
from django.contrib import admin
from conversation.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),

    url(r'^admin/', include(admin.site.urls)),
)
