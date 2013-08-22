from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^private/$', 'underlist.core.views.private', name='private'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}, name='login'),
    url(r'^register/$', 'underlist.core.views.register', name='register'),
    url(r'^logout/$', 'underlist.core.views.logout_user', name='logout'),

	#Static
	url(r'^about/$', TemplateView.as_view(template_name="core/about.html")),

)
