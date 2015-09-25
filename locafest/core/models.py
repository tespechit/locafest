# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from django_extensions.db.fields import AutoSlugField


UF_CHOICES = Choices(
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', overwrite=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', overwrite=True)
    category = models.ForeignKey('Category', related_name='products')
    image = models.ImageField(upload_to='products')
    rent_price = models.DecimalField(max_digits=5, decimal_places=2)
    reposition_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    celphone = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        db_table = "clients"

    def __str__(self):
        return self.name


class Order(models.Model):

    METHOD_PAYMENTS = Choices(
        ('money', _('Money')),
        ('debit', _('Debit Card')),
        ('credit', _('Credit Card')),
        ('check', _('Check Sheet')),
    )

    number = models.AutoField()
    created_at = models.DateField(auto_now_add=True)
    returned_at = models.DateField()
    client = models.ForeignKey('Client', related_name='orders')
    method_payment = models.CharField(max_length=10, choices=METHOD_PAYMENTS)
    address = models.CharField(max_length=150, blank=True)
    number = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, choices=UF_CHOICES, blank=True)
    items = models.ManyToManyField('Product', through='OrderItems',
                                   through_fields=('order', 'product'))


class OrderItems(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey('Product')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "order_items"
