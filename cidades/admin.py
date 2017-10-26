from django.contrib import admin
from .models import Cidade
from cadastro_abrigos.models import Abrigo

class AbrigoInLine(admin.StackedInline):
	model = Abrigo
	extra = 1

class CidadeAdmin(admin.ModelAdmin):
	inlines = [AbrigoInLine]

admin.site.register(Cidade, CidadeAdmin)
