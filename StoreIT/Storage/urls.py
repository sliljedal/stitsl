from django.urls import path, include, re_path
from Storage.views import *


urlpatterns = [
    re_path('^item/detail/(?P<pk>\d+)/', ItemDetailView.as_view(), name='item-detail'),
    re_path('^item/list/', ItemListView.as_view(), name='item-list'),
    ]

