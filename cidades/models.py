from django.db import models
from django.contrib.auth.models import User

class Cidade(models.Model):
    estados = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=estados, verbose_name='UF')
    usuario = models.OneToOneField(User)
    # pontos_de_distribuicao = models.ForeignKey('Distribuicao', blank=True, null=True)

    def __str__(self):
        return self.nome
        