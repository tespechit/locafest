# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryList(APIView):
    """List all categories, or create a new"""
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """Retrieve update and delete a category"""

    def get_object(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        category = self.get_object(slug)
        category.delete()
        return Response(status=status.HTTP_200_OK)

