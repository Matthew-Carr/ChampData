from django.conf.urls import url
from . import views

urlpatterns = [
	# /championdata
	url(r'^$', views.index, name="index"),
	# /championdata/Ahri/
	url(r'^(?P<champion>[a-z | A-Z | 0-9 | _]+)/$', views.detail, name='detail'),
	url(r'^(?P<champion1>[a-z | A-Z | 0-9 | _]+)/(?P<champion2>[a-z | A-Z | 0-9 | _]+)/$', views.compare, name='compare'),
	
]














