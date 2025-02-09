# Generated by Django 2.2 on 2021-05-14 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0083_auto_20210514_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 18, 3, 28, 410183), verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='instock_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 14, 18, 3, 28, 410183), null=True, verbose_name='上架日期'),
        ),
    ]
