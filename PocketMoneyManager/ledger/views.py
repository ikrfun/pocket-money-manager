from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return HttpResponse('Hello World')