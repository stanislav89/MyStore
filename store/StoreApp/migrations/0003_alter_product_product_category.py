# Generated by Django 3.2.6 on 2021-08-14 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0002_auto_20210813_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreApp.category'),
        ),
    ]
