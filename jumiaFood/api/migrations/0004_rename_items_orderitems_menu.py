# Generated by Django 4.0.4 on 2022-06-19 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_order_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='items',
            new_name='menu',
        ),
    ]
