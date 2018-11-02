from django.db import models


class Cliente(models.Model):
    SEXO_CHOICES = (
        ('f', 'Feminino'),
        ('m', 'Masculino'),
    )
    nome = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
