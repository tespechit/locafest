# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models
from core.models import Product, Category, Client, Order


class CategoryTest(TestCase):
    def test_should_field_name(self):
        field = Category._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_slug(self):
        field = Category._meta.get_field('slug')
        self.assertIsInstance(field, models.SlugField)


class ProductTest(TestCase):
    def test_should_field_name(self):
        field = Product._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_category(self):
        field = Product._meta.get_field('category')
        self.assertIsInstance(field, models.ForeignKey)

    def test_should_field_image(self):
        field = Product._meta.get_field('image')
        self.assertIsInstance(field, models.ImageField)

    def test_should_field_rent_price(self):
        field = Product._meta.get_field('rent_price')
        self.assertIsInstance(field, models.DecimalField)

    def test_should_field_reposition_price(self):
        field = Product._meta.get_field('reposition_price')
        self.assertIsInstance(field, models.DecimalField)


class ClientTest(TestCase):
    def test_should_field_name(self):
        field = Client._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_cpf(self):
        field = Client._meta.get_field('cpf')
        self.assertIsInstance(field, models.IntegerField)

    def test_should_field_rg(self):
        field = Client._meta.get_field('rg')
        self.assertIsInstance(field, models.IntegerField)

    def test_should_field_celphone(self):
        field = Client._meta.get_field('celphone')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_phone(self):
        field = Client._meta.get_field('phone')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_email(self):
        field = Client._meta.get_field('email')
        self.assertIsInstance(field, models.EmailField)


class OrderTest(TestCase):
    def test_should_field_number(self):
        field = Order._meta.get_field('number')
        self.assertIsInstance(field, models.IntegerField)

    def test_should_field_created_at(self):
        field = Order._meta.get_field('created_at')
        self.assertIsInstance(field, models.DateField)

    def test_should_field_returned_at(self):
        field = Order._meta.get_field('returned_at')
        self.assertIsInstance(field, models.DateField)

    def test_should_field_client(self):
        field = Order._meta.get_field('client')
        self.assertIsInstance(field, models.ForeignKey)

    def test_should_field_method_payment(self):
        field = Order._meta.get_field('method_payment')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_address(self):
        field = Order._meta.get_field('address')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_number(self):
        field = Order._meta.get_field('number')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_district(self):
        field = Order._meta.get_field('district')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_city(self):
        field = Order._meta.get_field('city')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_state(self):
        field = Order._meta.get_field('state')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_items(self):
        field = Order._meta.get_field('items')
        self.assertIsInstance(field, models.ManyToManyField)
