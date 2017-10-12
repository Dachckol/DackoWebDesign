from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'pages.views.home'),
                       url(r'^home/$', 'pages.views.home'),
                       url(r'^about/$', 'pages.views.about'),
                       url(r'^faq/$', 'pages.views.faq'),
                       )
