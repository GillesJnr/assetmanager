from django.contrib import admin
from .models import *

# Register your models here.


class ServiceTypeAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'servicetype')
    list_filter = ['servicetype']


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'company')
    list_filter = ['company']


class UserPasswordAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'username', 'password')
    list_filter = ['account']


class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'type', 'serial_number', 'purchase_date')


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(UserPassword, UserPasswordAdmin)
admin.site.register(AssetType,AssetTypeAdmin)
admin.site.register(Asset, AssetAdmin)