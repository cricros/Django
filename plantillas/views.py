# para hacer el render de las vistas (templates)
from django.shortcuts import render

def simple(request, name):
    return render(request, 'simple.html',{}) #aqui va el contexto

def dinamico(request, name):
    context = {'name': name}
    return render(request, 'dinamico.html',context)