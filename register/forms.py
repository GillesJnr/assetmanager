from django.forms import ModelForm
from .models import *


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'company', 'serial_number', 'type']


class AssetTypeForm(ModelForm):
    class Meta:
        model = AssetType
        fields = '__all__'