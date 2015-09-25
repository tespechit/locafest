# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy
from core.models import Category


class CategoryTest(APITestCase):
    def setUp(self):
        self.category = mommy.make(Category, name="Category 01")

    def test_get_categories(self):
        """GET /categories must return status code 200"""
        url = reverse('api:categories-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'id': 1,
                'slug': 'category-01',
                'name': 'Category 01'
            }
        ])

    def test_post_categories(self):
        """POST /categories must create and return status code 201"""
        url = reverse('api:categories-list')
        data = {
            'name': 'Other Category'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.last().name, 'Other Category')

    def test_get_category(self):
        """GET /categories/{slug} must return status code 200"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'slug': 'category-01',
            'name': 'Category 01'
        })

    def test_put_category(self):
        """PUT /categories/{slug} must update a category"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        data = response.data
        data['name'] = 'Category 02'

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.last().name, 'Category 02')
        self.assertEqual(Category.objects.last().slug, 'category-02')

    def test_delete_category(self):
        """DELETE /categories/{slug} must remove a category"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_category(self):
        """GET /categories/{slug} not must return a nonexistent category"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})
        self.category.delete()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_nonexistent_category(self):
        """PUT /categories/{slug} not must update a nonexistent category"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        data = response.data
        data['name'] = 'Category 02'

        self.category.delete()

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_category(self):
        """DELETE /categories/{slug} not must remove a nonexistent category"""
        url = reverse('api:categories-details',
                      kwargs={'slug': self.category.slug})

        self.category.delete()

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
