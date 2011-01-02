from django.conf.urls.defaults import *

urlpatterns = patterns('champion_manager.views',
	url(r'^(?P<slug>[0-9A-z_\-]+)/$', 'city', name='city'),
)