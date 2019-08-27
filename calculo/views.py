from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from calculo.serializer import CalculoSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework import viewsets 

# Create your views here.
class CalculoViewSet(viewsets.ViewSet):

    serializer_class = CalculoSerializer
    queryset = User.objects.all()

#    def list(self, request):
#        queryset = User.objects.all()
#        serializer = CalculoSerializer(queryset, many=True)
#        return Response(serializer.data)

#    def retrieve(self, request, pk=None):
#        queryset = User.objects.all()
#        user = get_object_or_404(queryset, pk=pk)
#        serializer = CalculoSerializer(user)
#        return Response(serializer.data)