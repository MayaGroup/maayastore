# Generated by Django 3.1.4 on 2020-12-19 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20201217_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 19, 18, 10, 58, 31882)),
        ),
    ]
