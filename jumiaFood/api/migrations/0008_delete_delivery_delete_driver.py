# Generated by Django 4.0.4 on 2022-07-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_orderitems_timestamp_order_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
    ]
