from django import urls
from django.urls import path


from . import views
import ledger


urlpatterns = [
    path('', views.index, name = 'index'),
    path('list', views.list.as_view(), name = 'list'),
    
    
]
