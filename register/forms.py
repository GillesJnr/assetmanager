from django.forms import ModelForm
from .models import *
from django import forms


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


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['servicetype'].empty_label = 'Select Service Type'


class UserPasswordForm(ModelForm):
    class Meta:
        model = UserPassword
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserPasswordForm, self).__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'Select User'


class ServiceTypeForm(ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Select Company'