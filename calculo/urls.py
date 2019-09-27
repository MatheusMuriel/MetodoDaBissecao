from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^calculo/$', calcular, name='calcular'),
    url(r'^gauss/$', gauss, name='gauss'),
    url('', index_view),
]