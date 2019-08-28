from rest_framework import generics
from .models import Calculo
from .serializer import CalculoSerializer
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
from .calculadora import factor

@csrf_exempt
def calcular(request):
	if request.method == 'POST':
		dados = str(request.body)
		v = spliter_request(dados)
		c = executarCalculo(v[0], v[1], v[2], v[3], v[4], v[5])
		return HttpResponse("a")
	pass

def spliter_request(dados):
	dados_limpos = re.sub(r"(\[|\]|\\|\'|b|\")","",dados)
	return dados_limpos.split(",")

def executarCalculo(x5, x4, x3, x2, x1, x):
	calc = factor(x5, x4, x3, x2, x1, x)
	calc.calcular()