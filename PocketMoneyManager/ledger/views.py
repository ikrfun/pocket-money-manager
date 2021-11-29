from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
# Create your views here.
def index(request):
    return render(request, 'detail/home.html')

class list(TemplateView):
    pass