from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from .models import *
# Create your views here.


def home(request):
    companies = Company.objects.all()
    company_count = companies.aggregate(Sum('id'))['id__sum']

    staffs = Staff.objects.all()
    staff_count = staffs.aggregate(Sum('id'))['id__sum']

    assets = Asset.objects.all()
    asset_count = assets.aggregate(Sum('id'))['id__sum']

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


def assettype(request):
    return render(request, "register/assettype/index.html")


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