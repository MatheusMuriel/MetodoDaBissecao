from rest_framework import generics
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
from .calculadora import factor
from .gauss import factory
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

@csrf_exempt
def calcular(request):
	if request.method == 'POST':
		dados = str(request.body)
		v = spliter_request(dados)
		c = executarCalculo(v[0], v[1], v[2], v[3], v[4], v[5], v[6])
		sc = serializadorDeResposta(c)
		return HttpResponse(sc)


def spliter_request(dados):
	dados_limpos = re.sub(r"(\[|\]|\\|\'|b|\")","",dados)
	return dados_limpos.split(",")

@csrf_exempt
def gauss(request):
	if request.method == 'POST':
		dados = str(request.body)
		v = spliter_request_gauss(dados)
		c = executarCalculoGauss(v)
		#sc = serializadorDeResposta(c)
		return HttpResponse('AAAAAAAAAAAAAAAAAAA')
	pass

def spliter_request_gauss(dados):
	str_limpa = dados[2:-1]
	arrDados = re.sub(r"({|}|\")","", str_limpa).split(",")
	dictMaptriz = {}
	for item in arrDados:
		arrItem = item.split(":")
		chave = arrItem[0]
		valor = float(arrItem[1])
		dictMaptriz[chave] = valor
		

	return dictMaptriz


"""
Cada intervalor começa e termina com $$$
Seguido por a::b=>
"""
def serializadorDeResposta(lista_resposta):
	resposta = ""

	#Cada objeto
	for intervalo in lista_resposta:
		resposta += "$$$"

		a = intervalo.a
		b = intervalo.b
		resposta += ("{}::{}".format(a, b))

		d = intervalo.iteracoes
		for chave, valor in d.items():
			resposta += "#{}[".format(chave)
			for vl in valor:
				resposta += "{};".format(vl)
			resposta += "]"

		print(resposta)

	print(resposta)
	
	return(resposta)


def executarCalculo(x5, x4, x3, x2, x1, x, epsilon):
	calc = factor(x5, x4, x3, x2, x1, x, epsilon)
	return calc.calcular()
def executarCalculoGauss(dictMap):
	gauss = factory(dictMap)
	return gauss.calcular()