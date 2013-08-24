from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin22/', include(admin.site.urls)),
    url(r'^', include('underlist.core.urls'), namespace='core'),
	url(r'^', include('underlist.backlog.urls'), namespace='backlog'),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)