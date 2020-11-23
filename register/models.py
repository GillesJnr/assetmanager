from django.db import models

# Create your models here.


class ServiceType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    servicetype = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return " %s %s" % (self.first_name, self.last_name)


class UserPassword(models.Model):
    name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    account = models.CharField(max_length=50)
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.account


class AssetType(models.Model):
    name = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=90)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=90, blank=True, null=True, unique=True)
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
