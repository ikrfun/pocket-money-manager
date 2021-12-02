from django import forms
from .models import Pay, Incom

class PayForm(forms.ModelForm):

    class Meta:
        model = Pay
        fields = ('name','price')

class IncomForm(forms.ModelForm):

    class Meta:
        model = Incom
        fields = ('name','price')

