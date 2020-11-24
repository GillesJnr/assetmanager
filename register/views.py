from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from .models import *
from .forms import *
# Create your views here.


def home(request):
    companies = Company.objects.all()
    company_count = companies.aggregate(Count('id'))['id__count']

    staffs = Staff.objects.all()
    staff_count = staffs.aggregate(Count('id'))['id__count']

    assets = Asset.objects.all()
    asset_count = assets.aggregate(Count('id'))['id__count']

    context = {
        'companies': companies,
        'company_count': company_count,
        'staffs': staffs,
        'staff_count': staff_count,
        'assets': assets,
        'asset_count': asset_count,
    }
    return render(request, "register/pages/layout.html", context)


def asset(request):
    assets = Asset.objects.all()
    context = {
        'assets': assets,
    }
    return render(request, "register/asset/index.html", context)


def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset')
        else:
            print("failed")
    else:
        form = AssetForm()
        return render(request, "register/asset/create-asset.html", {'form': form})


def update_asset(request, id):
    if request.method == "GET":
        asset = Asset.objects.get(pk=id)
        form = AssetForm(instance=asset)
        return render(request, "register/asset/create-asset.html", {'form': form})
    else:
        asset = Asset.objects.get(pk=id)
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
        return redirect('asset')


def delete_asset(request, id):
    asset = Asset.Objects.get(pk=id)
    asset.delete()
    return redirect('asset')


def asset_type(request):
    types = AssetType.objects.all()
    return render(request, "register/assettype/index.html", {'types': types})


def add_asset_type(request):
    if request.method == "GET":
        form = AssetTypeForm()
        return render(request, "register/assettype/create-asset-type.html", {'form': form})
    else:
        form = AssetTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_type')
        else:
            return render(request, 'register/assettype/create-asset-type.html', {'form': form})


def edit_asset_type(request, id):
    if request.method == "GET":
        assettype = AssetType.objects.get(pk=id)
        form = AssetTypeForm(instance=assettype)
        return render(request, 'register/assettype/create-asset-type.html', {'form': form})
    else:
        assettype = AssetType.objects.get(pk=id)
        form = AssetTypeForm(request.POST, instance=assettype)
        if form.is_valid():
            form.save()
            return redirect('asset_type')
        else:
            return render(request, 'register/assettype/create-asset-type.html', {'form': form})


def delete_asset_type(request, id):
    asset_type = AssetType.objects.get(pk=id)
    asset_type.delete()
    return redirect('asset_type')


def company(request):
    companies = Company.objects.all()
    return render(request, "register/company/index.html", {'companies': companies})


def add_company(request):
    if request.method == "GET":
        form = CompanyForm()
        return render(request, "register/company/create-company.html", {'form': form})
    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')
        else:
            return render(request, "register/company/create-company.html", {'form': form})



def update_company(request, id):
    if request.method == "GET":
        company = Company.objects.get(pk=id)
        form = CompanyForm(instance=company)
        return render(request, "register/company/create-company.html", {'form': form})
    else:
        company = Company.objects.get(pk=id)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company')
        else:
            return render(request, 'register/company/create-company.html', {'form': form})


def delete_company(request, id):
    company = Company.objects.get(pk=id)
    company.delete()
    return redirect('company')


def password(request):
    passwords = UserPassword.objects.all()
    return render(request, "register/password/index.html", {'passwords': passwords})


def add_password(request):
    if request.method == "GET":
        form = UserPasswordForm()
        return render(request, "register/password/user-details.html", {'form': form})
    else:
        form = UserPasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('password')
        else:
            return render(request, 'register/password/user-details.html', {'form': form})


def update_password(request, id):
    if request.method == "GET":
        password = UserPassword.objects.get(pk=id)
        form = UserPasswordForm(instance=password)
        return render(request, 'register/password/user-details.html', {'form': form})
    else:
        password = UserPassword.objects.get(pk=id)
        form = UserPasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            return redirect('password')
        else:
            return render(request, 'register/password/user-details.html', {'form': form})


def delete_password(request, id):
    password = UserPassword.objects.get(pk=id)
    password.delete()
    return redirect('password')


def service_type(request):
    services = ServiceType.objects.all()
    return render(request, "register/servicetype/index.html", {'services': services})


def add_service_type(request):
    if request.method == "GET":
        form = ServiceTypeForm()
        return render(request, 'register/servicetype/create-service-type.html', {'form': form})
    else:
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_type')
        else:
            return render(request, 'register/servicetype/create-service-type.html', {'form': form})


def update_service_type(request, id):
    servicetype = ServiceType.objects.get(pk=id)
    if request.method == "GET":
        form = ServiceTypeForm(instance=servicetype)
        return render(request, 'register/servicetype/create-service-type.html', {'form': form})
    else:
        form = ServiceTypeForm(request.POST, instance=servicetype)
        if form.is_valid():
            form.save()
            return redirect('service_type')
        else:
            return render(request, 'register/servicetype/create-service-type.html', {'form': form})


def delete_service_type(request, id):
    servicetype = ServiceType.objects.get(pk=id)
    servicetype.delete()
    return redirect('service_type')


def staff(request):
    staffs = Staff.objects.all()
    return render(request, "register/staff/index.html", {'staffs': staffs})


def add_staff(request):
    if request.method == "GET":
        form = StaffForm()
        return render(request, "register/staff/create-staff.html", {'form': form})
    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
        else:
            return render(request, "register/staff/create-staff.html", {'form': form})


def update_staff(request, id):
    staffs = Staff.objects.get(pk=id)
    if request.method == "GET":
        form = StaffForm(instance=staffs)
        return render(request, "register/staff/create-staff.html", {'form': form})
    else:
        form = StaffForm(request.POST, instance=staffs)
        if form.is_valid():
            form.save()
            return redirect('staff')
        else:
            return render(request, "register/staff/create-staff.html", {'form': form})


def delete_staff(request, id):
    staffs = Staff.objects.get(pk=id)
    staffs.delete()
    return redirect('staff')