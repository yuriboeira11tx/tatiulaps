from django.db import models
from cidades.models import Cidade

class Abrigo(models.Model):
	nome = models.CharField(max_length = 80)
	cidade = models.ForeignKey(Cidade, null=True)
	rua = models.CharField(max_length = 90)
	bairro = models.CharField(max_length = 30)
	numero = models.PositiveIntegerField()
	capacidade = models.PositiveIntegerField()

	def __str__(self):
		return self.nome
