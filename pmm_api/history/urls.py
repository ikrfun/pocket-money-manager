from django.urls import path
from . import views
from rest_framework import routers
from .views import IncomViewSet,PayViewSet

router = routers.DefaultRouter()
router.register('pay/',PayViewSet)
router.register('incom/',IncomViewSet)