# Generated by Django 3.1.1 on 2020-11-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201124_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address2',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone_no',
            field=models.CharField(default='', max_length=15),
        ),
    ]
