from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('ergocoin.views',
    url(r'^$', 'homepage', name='homepage'),
)
