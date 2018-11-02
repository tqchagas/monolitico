from django.db import models


class Hotel(models.Model):
    nome = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    valor_diaria = models.DecimalField(
        max_digits=6, decimal_places=2, default=100.00)

    def __str__(self):
        return '{} R$ {}/dia'.format(self.nome, self.valor_diaria)
