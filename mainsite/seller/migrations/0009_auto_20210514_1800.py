# Generated by Django 2.2 on 2021-05-14 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_auto_20210514_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerwithdrawrecord',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 18, 0, 47, 408383), verbose_name='儲存日期'),
        ),
    ]
