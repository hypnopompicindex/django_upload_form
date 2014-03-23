from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^create/$', 'upload_form.views.create'),
)