# Generated by Django 2.0.7 on 2018-07-30 04:20

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('orders', '0002_auto_20180730_0320'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItems',
            new_name='MenuItem',
        ),
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
