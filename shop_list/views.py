from shop_list.models import Item
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class Shoplist(ListView):
  template_name = "shop_list/index.html"
  model = Item
  context_object_name = "items"

  