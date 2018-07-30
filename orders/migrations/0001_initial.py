# Generated by Django 2.0.7 on 2018-07-30 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCategory', models.CharField(max_length=200)),
                ('itemSubCategory', models.CharField(max_length=200)),
                ('itemName', models.CharField(max_length=200)),
                ('itemGroup', models.CharField(max_length=200)),
                ('unitPrice', models.FloatField()),
                ('itemSize', models.CharField(choices=[('S', 'Small'), ('L', 'Large'), ('N', 'NA')], max_length=1)),
                ('noOfTopping', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('orderStatus', models.CharField(choices=[('N', 'Not Placed'), ('O', 'Order Received'), ('I', 'Cooking'), ('R', 'Ready'), ('D', 'Delivered')], max_length=1)),
                ('order_date', models.DateTimeField(verbose_name='Ordered date')),
                ('totalPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('itemID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.MenuItems')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItems', to='orders.Order')),
            ],
        ),
    ]
