from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
     # ex: /enquete/5/
    path("<int:pk>/", views.DetalheView.as_view(), name="detalhe"),
    # ex: /enquete/5/resultados/
    path("<int:pk>/resultados/", views.ResultadosView.as_view(), name="resultados"),
    # ex: /enquete/5/voto/
    path("<int:questao_id>/voto/", views.voto, name="voto"),
]