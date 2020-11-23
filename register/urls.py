from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('asset', views.asset, name="asset"),
    path('add-asset', views.add_asset, name="add_asset"),
    path('<int:id>/', views.update_asset, name="update_asset"),
    path('delete/<int:id>/', views.delete_asset, name="delete_asset"),
    path('asset-type', views.asset_type, name="asset_type"),
    path('add-asset-type', views.add_asset_type, name="add_asset_type"),
    path('<int:id>/', views.update_asset_type, name="update_asset_type"),
    path('delete/<int:id>', views.delete_asset_type, name="delete_asset_type"),
]
