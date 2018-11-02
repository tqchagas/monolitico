from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from clientes.models import Cliente


class ListarCliente(ListView):
    model = Cliente


class VisualizarCliente(DetailView):
    model = Cliente


class NovoCliente(CreateView):
    model = Cliente
    fields = ['nome', 'sexo', 'telefone', 'celular', 'email', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
    success_url = reverse_lazy('listar_cliente')


class EditarCliente(UpdateView):
    model = Cliente
    fields = ['nome', 'sexo', 'telefone', 'celular', 'email', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
    success_url = reverse_lazy('listar_cliente')


class ApagarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('listar_cliente')
