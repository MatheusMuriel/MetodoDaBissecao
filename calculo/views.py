from rest_framework import generics
from .models import Calculo
from .serializer import CalculoSerializer
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
from .calculadora import factor
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.templatetags.staticfiles import static

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

def home(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render({},request))

@csrf_exempt
def calcular(request):
	if request.method == 'POST':
		dados = str(request.body)
		v = spliter_request(dados)
		c = executarCalculo(v[0], v[1], v[2], v[3], v[4], v[5], v[6])
		return HttpResponse("a")
	pass

def spliter_request(dados):
	dados_limpos = re.sub(r"(\[|\]|\\|\'|b|\")","",dados)
	return dados_limpos.split(",")

def executarCalculo(x5, x4, x3, x2, x1, x, epsilon):
	calc = factor(x5, x4, x3, x2, x1, x, epsilon)
	calc.calcular()