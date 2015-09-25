# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models
from authentication.models import User


class UserTest(TestCase):
    def test_should_a_field_email(self):
        field = User._meta.get_field('email')
        self.assertIsInstance(field, models.EmailField)

    def test_should_a_field_username(self):
        field = User._meta.get_field('username')
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(40, field.max_length)
        self.assertTrue(field.unique)


    def test_should_a_field_name(self):
        field = User._meta.get_field('name')
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(50, field.max_length)

    def test_should_a_field_created_at(self):
        field = User._meta.get_field('created_at')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_a_field_updated_at(self):
        field = User._meta.get_field('updated_at')
        self.assertIsInstance(field, models.DateTimeField)
