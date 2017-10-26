from django.db import models
from cidades.models import Cidade
y = 21 + 21 #batainha quando nasce esparrama for the ground. Olá meu povo lindO. 
class Incidente(models.Model):
	gravidades = (
		('AC','Acidente'),
		('DMP', 'Médio Porte'),
		('DGP', 'Grande Porte'),
		('DMGP', 'Muito Grande Porte'),
	)

	cidade = models.ForeignKey(Cidade)
	tipo = models.CharField(max_length=30)
	#batata = models.DateField()
	data_prevista = models.DateField()
	gravidade = models.CharField(max_length=4, choices=gravidades)
	postado_por = models.ForeignKey('auth.User', editable=False)
