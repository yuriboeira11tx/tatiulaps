from django.db import models
from django.contrib.auth.models import User

class Especialista(models.Model):
	nome = models.CharField(max_length=50)
	especialidade = models.CharField(max_length=100)
	usuario = models.OneToOneField(User)
