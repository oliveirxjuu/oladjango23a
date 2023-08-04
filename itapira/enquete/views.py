from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Questao, Resposta


# Create your views here.

class IndexView(generic.ListView):
    model = Questao
    template_name = 'enquete/index.html'


class DetalheView(generic.DetailView):
    model = Questao
    template_name = 'enquete/detalhe.html'


class ResultadosView(generic.DetailView):
    model = Questao
    template_name = 'enquete/resultado.html'


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        resposta = questao.resposta_set.get(pk=request.POST["resposta"])
    except (KeyError, Resposta.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "enquete/questao.html",
            {
                "questao": questao,
                "error_message": "Esta Resposta naum ecxiste.",
            },
        )
    else:
        resposta.votos += 1
        resposta.save()
        return HttpResponseRedirect(reverse("resultados", args=(questao.id,)))