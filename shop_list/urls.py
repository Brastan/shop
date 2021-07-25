from django.urls import path

from . import views

urlpatterns = [
  path("", views.Shoplist.as_view(), name="shoplist")
]