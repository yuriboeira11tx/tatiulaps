from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_cidade(user):
	return str(user.groups.first()) == 'Cidades'

@user_passes_test(is_cidade)
@login_required
def main(request):
	return render(request, 'cidades/main.html')
