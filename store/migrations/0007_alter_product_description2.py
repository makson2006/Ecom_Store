# Generated by Django 5.0.1 on 2024-02-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_description2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description2',
            field=models.TextField(blank=True, default='', max_length=10000, null=True),
        ),
    ]
