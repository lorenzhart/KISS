from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'intro.introapp.views.index'),
    url(r'^search/(?P<key>.*)/(?P<tag>.*)/$', 'intro.introapp.views.index')
)

#    url(r'^search/(?P<key>\w*)/(?P<value>\w*)/$', 'intro.introapp.views.index')

