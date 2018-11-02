from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from vendas.models import Venda, VendaComissao


class ListarVenda(ListView):
    model = Venda


class VisualizarVenda(DetailView):
    model = Venda


class NovaVenda(CreateView):
    model = Venda
    fields = ['cliente', 'voo_ida', 'voo_volta', 'hotel', 'diarias', 'data_viagem']
    success_url = reverse_lazy('listar_venda')

    def form_valid(self, form):
        response = super(NovaVenda, self).form_valid(form)
        comissao = self.object.hotel.valor_diaria * self.object.diarias
        VendaComissao.objects.create(
            venda=self.object,
            comissao=comissao
        )
        return response


class ApagarVenda(DeleteView):
    model = Venda
    success_url = reverse_lazy('listar_venda')


class RelatorioVendas(View):
    def get(self, request):
        comissoes = VendaComissao.objects.all()
        total = comissoes.aggregate(Sum('comissao'))
        return render(
            request,
            'vendas/comissoes.html',
            {
                'comissoes': comissoes,
                'total': total['comissao__sum']
            }
        )
