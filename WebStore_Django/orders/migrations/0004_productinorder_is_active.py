# Generated by Django 2.2.15 on 2020-08-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200813_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
