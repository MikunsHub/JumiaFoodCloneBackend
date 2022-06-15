# Generated by Django 4.0.4 on 2022-06-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', to='api.menu'),
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
    ]
