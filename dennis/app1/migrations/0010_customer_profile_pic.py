# Generated by Django 3.1.5 on 2021-04-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
