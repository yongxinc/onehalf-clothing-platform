# Generated by Django 2.2 on 2021-05-16 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_auto_20210516_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerwithdrawrecord',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 17, 48, 37, 821179), verbose_name='儲存日期'),
        ),
    ]
