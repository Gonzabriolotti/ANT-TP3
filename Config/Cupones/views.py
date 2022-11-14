from django.shortcuts import render
from rest_framework import viewsets

from .serializer import CuponesSerializer
from .models import Coupons

# Create your views here.

class CuponesViewSet(viewsets.ModelViewSet):
    queryset = Coupons.objects.all().order_by('code')
    serializer_class = CuponesSerializer

