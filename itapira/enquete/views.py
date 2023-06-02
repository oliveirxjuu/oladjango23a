from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Questao

# Create your views here.

def index(request):
    # selecionar na tabela questoes os ultimos 5 objetos cadastrados
    ultimas_questoes = Questao.objects.order_by("data")[:5]
    # criamos um dicionario em python
    # (semelhante aos arryas associativos do php)
    # (ou aos arryas objetos literais do javascript)
    # onde passamos essa variavel para ser utilizada no template
    context = {'ultimas_questoes': ultimas_questoes}
    # retornar a funcao render, passando como argumentos
    # a requisicao, o template que sera utilizado
    # e as variaveis de contexto que serao utilizadas dentro do template
    return render(request, 'enquete/index.html', context)


def caneta(request):
    return HttpResponse("<h1>Caneta Azul, Azul caneta...</h1>")


def detalhe(request, questao_id):
    try:
        questao = Questao.objects.get(pk=questao_id)
    except Questao.DoesNotExist:
        raise Http404("Questão não ecxisty")
    return render(request, 'enquete/detalhe.html', {'questao': questao})


def resultados(request, questao_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Voce esta votando na questao %s." % questao_id)