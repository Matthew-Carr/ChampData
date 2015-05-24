from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<summoner_name>[a-z | A-Z | 0-9 | _]+)/$', views.summoner_info, name='info')
	]
