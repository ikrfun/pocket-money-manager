from django.shortcuts import render
from .models import Pay,Incom
from rest_framework import viewsets,filters
from .serializer import PaySerializer,IncomSerializer

class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer

class IncomViewSet(viewsets.ModelViewSet):
    queryset = Incom.objects.all()
    serializer_class = IncomSerializer