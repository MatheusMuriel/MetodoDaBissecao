
from rest_framework import serializers
from .models import Calculo

class CalculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Calculo

        #Serializando todos os itens de calculo.
        fields = '__all__' 

        #Caso se queira serializar apenas alguns itens:
        #fields = ('funcao', 'epsilon')
