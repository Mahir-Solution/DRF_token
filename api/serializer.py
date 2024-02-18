from rest_framework import serializers
from .models import Chair

class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = ['id','model','color','address','price']
