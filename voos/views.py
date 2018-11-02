from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from voos.models import Voo


class ListarVoo(ListView):
    model = Voo


class VisualizarVoo(DetailView):
    model = Voo


class NovoVoo(CreateView):
    model = Voo
    fields = ['origem', 'destino', 'numero', 'partida', 'chegada', 'valor']
    success_url = reverse_lazy('listar_voo')


class EditarVoo(UpdateView):
    model = Voo
    fields = ['origem', 'destino', 'numero', 'partida', 'chegada', 'valor']
    success_url = reverse_lazy('listar_voo')


class ApagarVoo(DeleteView):
    model = Voo
    success_url = reverse_lazy('listar_voo')
