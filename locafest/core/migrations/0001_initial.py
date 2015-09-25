# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, populate_from='name', editable=False, overwrite=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('rg', models.IntegerField()),
                ('celphone', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('returned_at', models.DateField()),
                ('method_payment', models.CharField(max_length=10, choices=[('money', 'Money'), ('debit', 'Debit Card'), ('credit', 'Credit Card'), ('check', 'Check Sheet')])),
                ('address', models.CharField(max_length=150, blank=True)),
                ('number', models.CharField(max_length=20, blank=True)),
                ('district', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=80, blank=True)),
                ('state', models.CharField(max_length=80, blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')])),
                ('client', models.ForeignKey(to='core.Client', related_name='orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(to='core.Order')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, populate_from='name', editable=False, overwrite=True)),
                ('image', models.ImageField(upload_to='products')),
                ('rent_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('reposition_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('category', models.ForeignKey(to='core.Category', related_name='products')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(to='core.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.Product', through='core.OrderItems'),
        ),
    ]
