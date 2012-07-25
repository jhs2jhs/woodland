from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello', 'main_code.views.hello'),
    url(r'^test_file_view', 'main_code.views.test_file'),
    url(r'^test_file_upload', 'main_code.views.test_file_upload'),

    url(r'^photo_upload$', 'main_code.views.photo_upload'),
    url(r'^photo_view$', 'main_code.views.photo_view'),
    url(r'^photo_comment_view$', 'main_code.views.photo_comment_view'),
    url(r'^comment_make$', 'main_code.views.comment_make'),

    
    url(r'^demo_photo_upload$', 'main_code.views.demo_photo_upload'),
    url(r'^photo_view$', 'main_code.views.photo_view'),
    url(r'^photo_comment_view$', 'main_code.views.photo_comment_view'),
    url(r'^demo_comment_make$', 'main_code.views.demo_comment_make'),      

)
