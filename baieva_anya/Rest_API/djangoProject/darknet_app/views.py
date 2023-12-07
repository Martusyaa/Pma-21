from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Products
from .serializer import ProductsSerializer


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer