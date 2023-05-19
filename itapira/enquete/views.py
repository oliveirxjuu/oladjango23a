from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Olha, se voce nao me ama</h1><h2>Caneta azul, azul caneta</h2>")

def caneta(request):
    return HttpResponse("<h1>Caneta Azul, Azul caneta...</h1>")


def detalhe(request, questao_id):
    return HttpResponse("Voce esta olhando a questao %s." % questao_id)


def resultados(request, questao_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Voce esta votando na questao %s." % questao_id)