# Generated by Django 3.1.5 on 2021-03-31 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20210331_1158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]