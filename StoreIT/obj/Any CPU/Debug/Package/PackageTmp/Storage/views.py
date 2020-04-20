from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from Storage.models import *

class ItemDetailView(DetailView):
    model = Item
    template_name = "storage/item-detail.html"

class StorageDetailView(DetailView):
    model = Storage

class BoxDetailView(DetailView):
    model = Box

class ItemListView    (ListView):
    model = Item   
    template_name = "storage/item-list.html"
    
class StorageListView (ListView):
    model = Storage
    
class BoxListView     (ListView):
    model = Box