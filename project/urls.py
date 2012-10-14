#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
#from .sitemaps import sitemaps

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stefanfoulis.views.home', name='home'),
    # url(r'^stefanfoulis/', include('stefanfoulis.foo.urls')),

#    url(r'^$', Home.as_view()),
#    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', 'core.views.upload', name="upload_binary_file"),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {'insecure': True}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('',
    url(r'^', include('filer.server.urls')),
    url(r'^', include('cms.urls')),
)
