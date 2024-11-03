from django.urls import path
from . import views

urlpatterns = [
    path("registrar-visitante/", views.registrar_visitantes, name="registrar_visitante"),
    path("visitante/<int:id>/", views.informacoes_visitantes, name="informacoes_visitante"),
    path("visitante/<int:id>/finalizar-visita/", views.finalizar_visita, name="finalizar_visita"),
]
