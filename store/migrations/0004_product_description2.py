# Generated by Django 5.0.1 on 2024-02-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description2',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]