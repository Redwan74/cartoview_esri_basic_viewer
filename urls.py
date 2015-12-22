from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name="%s.home" % views.APP_NAME),
    url(r'^new/$', views.new, name='%s.new'% views.APP_NAME),
     url(r'^view/(?P<resource_id>\d+)/$', views.view, name='%s.view'% views.APP_NAME),
     url(r'^edit/(?P<resource_id>\d+)/$', views.edit, name='%s.edit'% views.APP_NAME),
)