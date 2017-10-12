from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'pages.views.home'),
                       url(r'^home/$', 'pages.views.home'),
                       url(r'^pages/', include('pages.urls')),
                       url(r'^portfolio/', include('portfolio.urls')),
                       url(r'^pricing/', include('pricing.urls')),
                       url(r'^contact/', include('contact.urls')),
                       url(r'^news/', include('news.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
