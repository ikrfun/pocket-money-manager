from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
# Create your views here.
from .forms import PayForm, IncomForm
def index(request):
    return render(request, 'detail/home.html')

class list(TemplateView):
    pass

def pay_form(request):
    form = PayForm()
    return render(request, 'detail/pay_form.html',{'form':form})

def incom_form(request):
    form = IncomForm()
    return render(request, 'detail/incom_form.html',{'form':form})