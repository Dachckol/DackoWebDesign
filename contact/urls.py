from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'contact.views.contact'),
                       url(r'^worked/$', 'contact.views.worked'),
                       )
