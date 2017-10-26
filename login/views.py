from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *

def get_group(request):
	return str(request.user.groups.first())

def fazer_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			usuario = authenticate(username=username, password=password)
			if usuario:
				login(request, usuario)
				return redirect('login:direcionar')
			return HttpResponse('Usuário ou Senha Inválidos!')
	else:
		form = LoginForm()
		return render(request, 'login/login.html', {'form': form})

@login_required
def direcionar(request):
	if get_group(request) == 'Cidades':
		return redirect('cidades:main')
	elif get_group(request) == 'Especialistas':
		return redirect('especialistas:main')
	else:
		return HttpResponse('OCORREU ALGUM ERRO')

@login_required
def fazer_logout(request):
	logout(request)
	return redirect("home:home")