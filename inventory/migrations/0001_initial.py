# Generated by Django 5.0.4 on 2024-05-06 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_available', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
    ]