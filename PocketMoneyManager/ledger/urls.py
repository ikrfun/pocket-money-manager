from django import urls
from django.urls import path


from . import views
import ledger


urlpatterns = [
    path('', views.index, name = 'index'),
    path('pay_list/', views.pay_list.as_view(), name = 'pay_list'),
    path('incom_list/', views.pay_list.as_view(), name = 'incom_list'),
    path('pay_form/',views.pay_form,name = 'pay_form'),
    path('incom_form/',views.incom_form,name = 'incom_form'),
]
