# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('core.urls', namespace='api')),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/auth/registration/', include('rest_auth.registration.urls')),
]
