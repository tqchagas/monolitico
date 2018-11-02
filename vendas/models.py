from django.db import models

from clientes.models import Cliente
from hoteis.models import Hotel
from voos.models import Voo


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    voo_ida = models.ForeignKey(
        Voo, on_delete=models.CASCADE, related_name='ida', null=True)
    voo_volta = models.ForeignKey(
        Voo, on_delete=models.CASCADE, related_name='volta', null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    diarias = models.IntegerField(null=True)
    data_viagem = models.DateField(null=True)
    realizada_em = models.DateTimeField(auto_now_add=True)


class VendaComissao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    comissao = models.DecimalField(
        max_digits=6, decimal_places=2, default=100.00)
