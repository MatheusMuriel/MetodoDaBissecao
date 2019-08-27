from rest_framework import generics
from .models import Calculo
from .serializer import CalculoSerializer
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calcular(request):
    if request.method == 'POST':
        #funcao = str(request.POST['funcao'])
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        return HttpResponse("a")
