from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from hoteis.models import Hotel


class ListarHotel(ListView):
    model = Hotel


class VisualizarHotel(DetailView):
    model = Hotel


class NovoHotel(CreateView):
    model = Hotel
    fields = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'valor_diaria']
    success_url = reverse_lazy('listar_hotel')


class EditarHotel(UpdateView):
    model = Hotel
    fields = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'valor_diaria']
    success_url = reverse_lazy('listar_hotel')


class ApagarHotel(DeleteView):
    model = Hotel
    success_url = reverse_lazy('listar_hotel')
