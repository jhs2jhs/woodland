from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello', 'main_code.views.hello'),
)
