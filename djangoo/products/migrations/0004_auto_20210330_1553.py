# Generated by Django 3.1.5 on 2021-03-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(null=True),
        ),
    ]