# Generated by Django 3.0.5 on 2024-12-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_product_description2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description2',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='none', max_length=5000),
        ),
    ]
