from rest_framework import serializers
from .models import Pay,Incom

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = '__all__'

class IncomSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = Incom
        fields = '__all__'