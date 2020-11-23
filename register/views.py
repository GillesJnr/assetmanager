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
    return render(request, "register/company/index.html")


def password(request):
    return render(request, "register/password/index.html")


def service(request):
    return render(request, "register/service/index.html")


def servicetype(request):
    return render(request, "register/servicetype/index.html")


def staff(request):
    return render(request, "register/staff/index.html")