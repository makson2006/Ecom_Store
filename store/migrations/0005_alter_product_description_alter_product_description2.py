# Generated by Django 5.0.1 on 2024-02-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_description2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description2',
            field=models.CharField(blank=True, default='', max_length=450, null=True),
        ),
    ]
