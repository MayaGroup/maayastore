# Generated by Django 3.0.6 on 2020-11-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(max_length=10000),
        ),
    ]