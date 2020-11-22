from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('asset', views.asset, name="asset"),
]
