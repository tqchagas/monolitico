from django.db import models


class Aeroporto(models.Model):
    sigla = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.sigla


class Voo(models.Model):
    origem = models.ForeignKey(
        Aeroporto, on_delete=models.CASCADE, related_name='origem')
    destino = models.ForeignKey(
        Aeroporto, on_delete=models.CASCADE, related_name='destino')
    numero = models.CharField(max_length=10)
    partida = models.DateTimeField()
    chegada = models.DateTimeField()
    valor = models.DecimalField(
        max_digits=6, decimal_places=2, default=100.00)

    def __str__(self):
        return 'Voo: {} -- {} <{}> - {} <{}>'.format(
            self.numero, self.origem, self.destino,
            self.partida.strftime('%d/%m/%Y %H:%M'),
            self.chegada.strftime('%d/%m/%Y %H:%M'),
        )
