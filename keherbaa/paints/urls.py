from django.conf.urls import patterns, include, url
from paints import views
from django.views.generic import ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	# url(r'^program/$', views.ProgramView.as_view(), name='program'),
	
)

urlpatterns += staticfiles_urlpatterns()