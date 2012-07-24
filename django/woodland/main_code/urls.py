from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello', 'main_code.views.hello'),
    url(r'^test_file_view', 'main_code.views.test_file'),
    url(r'^test_file_upload', 'main_code.views.test_file_upload'),
)
