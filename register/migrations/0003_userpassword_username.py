# Generated by Django 3.1.3 on 2020-11-21 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_userpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpassword',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=90),
            preserve_default=False,
        ),
    ]
