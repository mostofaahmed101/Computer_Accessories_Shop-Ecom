# Generated by Django 3.0.5 on 2024-12-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20241230_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=25),
        ),
    ]
