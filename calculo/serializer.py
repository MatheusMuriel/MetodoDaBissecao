
from rest_framework import serializers

from .models import Calculo

class CalculoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Calculo
