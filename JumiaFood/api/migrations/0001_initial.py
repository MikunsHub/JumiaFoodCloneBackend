# Generated by Django 4.0.4 on 2022-06-19 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
                ('vehicle_type', models.CharField(max_length=20)),
                ('driver_license', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('pending', 'pending'), ('delivered', 'delivered')], default='ordered', max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('no_of_establishments', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.business_type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', through='api.OrderItems', to='api.menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time', models.DateTimeField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
    ]
