"""keherbaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#for loading static files:
from django.conf.urls.static import static
from django.conf import settings

# from django.db.models.loading import cache as model_cache

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# if not model_cache.loaded:
#     model_cache.get_models()
   
admin.autodiscover()


urlpatterns = [
    url(r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('paints.urls',namespace = "paints")),
    url(r'^nested_admin/', include('nested_admin.urls')),
    # url(r'^tribune/', include('djangotribune.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()