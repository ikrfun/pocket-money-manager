from django import urls
from django.urls import path


from . import views
import ledger


urlpatterns = [
    path('', views.index, name = 'index'),  
]
