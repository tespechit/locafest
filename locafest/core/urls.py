# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import CategoryList, CategoryDetail

urlpatterns = [
    url(r'categories/$', CategoryList.as_view(), name='categories-list'),
    url(r'categories/(?P<slug>[\w-]+)/$', CategoryDetail.as_view(),
        name='categories-details'),
]
