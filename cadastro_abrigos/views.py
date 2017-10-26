from .models import Abrigo
from django.shortcuts import render

def indice(request):
	abrigos = Abrigo.objects.all()
	return render(request, 'abrigos/indice.html', {'abrigos': abrigos})
