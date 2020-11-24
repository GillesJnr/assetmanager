from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('asset', views.asset, name="asset"),
    path('add-asset', views.add_asset, name="add_asset"),
    path('asset/<int:id>', views.update_asset, name="update_asset"),
    path('delete/<int:id>/', views.delete_asset, name="delete_asset"),

    path('asset-type', views.asset_type, name="asset_type"),
    path('add-asset-type', views.add_asset_type, name="add_asset_type"),
    path('assettype/<int:id>', views.edit_asset_type, name="edit_asset_type"),
    path('delete/<int:id>', views.delete_asset_type, name="delete_asset_type"),

    path('company', views.company, name="company"),
    path('add-company', views.add_company, name="add_company"),
    path('company/<int:id>', views.update_company, name="update_company"),
    path('company/del/<int:id>', views.delete_company, name="delete_company"),



    path('password', views.password, name='password'),
    path('add-password', views.add_password, name='add_password'),
    path('password/<int:id>', views.update_password, name='update_password'),
    path('password/del/<int:id>', views.delete_password, name='delete_password'),
]
