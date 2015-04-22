from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', include('ChampData.urls'), name='home'),
    url(r'^championdata/', include('ChampData.urls', namespace="ChampData")),
    url(r'^about/', include('myInfo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
