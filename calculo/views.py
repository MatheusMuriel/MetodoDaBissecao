from rest_framework import generics
from .models import Calculo
from .serializer import CalculoSerializer
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

@csrf_exempt
def calcular(request):
    if request.method == 'POST':
        dados = str(request.body)
        valores = spliter_request(dados)

        return HttpResponse("a")

def spliter_request(dados):
	dados_limpos = re.sub(r"(\[|\]|\\|\'|b|\")","",dados)
	return dados_limpos.split(",")