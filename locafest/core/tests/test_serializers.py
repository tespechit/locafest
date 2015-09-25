# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy
from core.models import Category
from core.serializers import CategorySerializer


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = mommy.make(Category, name="Category 01")

    def test_serialize_category(self):
        """Should serializer category to JSON format"""
        serializer = CategorySerializer(self.category)
        output_json = {
            'id': 1,
            'slug': 'category-01',
            'name': 'Category 01'
        }
        self.assertEqual(output_json, serializer.data)
