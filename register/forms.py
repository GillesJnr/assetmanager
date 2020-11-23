from django.forms import ModelForm
from .models import *


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'company', 'serial_number', 'type']

    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Select Company'
        self.fields['type'].empty_label = 'Select Type'


class AssetTypeForm(ModelForm):
    class Meta:
        model = AssetType
        fields = '__all__'

