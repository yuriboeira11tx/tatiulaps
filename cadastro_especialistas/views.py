from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from cadastro_incidente.models import Incidente
from cadastro_abrigos.models import Abrigo
from .forms import IncidenteForm
import smtplib

def is_especialista(user):
	return str(user.groups.first()) == 'Especialistas'

@user_passes_test(is_especialista)
@login_required(login_url='/login/')
def main(request):
	return render(request, 'especialistas/main.html')

@login_required(login_url='/login/')
@user_passes_test(is_especialista)
def cadastro(request):
	if request.method == 'POST':
		def enviar(incidente):
			email = 'tiltaps.hunters@gmail.com'
			senha = 'ricardo_sempre_atento'
			abrigos = Abrigo.objects.filter(cidade=incidente.cidade)
			qtd_abrigos = len(abrigos)
			responsavel = incidente.postado_por
			cidade = incidente.cidade
			destinatario = incidente.cidade.usuario.email
			tipo = incidente.tipo
			gravidade = incidente.gravidade

			mensagem = '''Subject: ALERTA de {}

- Segundo {}, o município de <span style="color:red;"{}</style> será vítima de <span style="color:red;"{}</style> no dia <span style="color:red;"{}</style>, sendo um evento de <span style="color:red;"{}</style>! 
- Há <span style="color:#08c;"{}</style> abrigos nesta área.
- Recomendamos manter a atenção redobrada para qualquer sinal de risco.'''.format(tipo, responsavel, cidade, tipo, data_prevista, gravidade, qtd_abrigos)

			server = smtplib.SMTP('smtp.gmail.com:587')
			
			server.starttls()
			server.ehlo()
			server.login(email, senha)
			server.sendmail(email, [destinatario], mensagem.encode('utf-8'))
			server.quit()

		form = IncidenteForm(request.POST)
		if form.is_valid():
			cidade = form.cleaned_data['cidade']
			tipo = form.cleaned_data['tipo']
			gravidade = form.cleaned_data['gravidade']
			data_prevista = form.cleaned_data['data_prevista']
			postado_por = request.user
			if Incidente.objects.create(cidade=cidade, tipo=tipo, gravidade=gravidade, data_prevista=data_prevista, postado_por=postado_por):
				enviar(Incidente.objects.get(cidade=cidade, tipo=tipo, gravidade=gravidade, data_prevista=data_prevista, postado_por=postado_por))
				return redirect('especialistas:indice')
	else:
		form = IncidenteForm()

	return render(request, 'especialistas/cadastro.html', {'form': form})

@user_passes_test(is_especialista)
@login_required
def indice(request):
	usuario = request.user
	incidentes = Incidente.objects.filter(postado_por=usuario).order_by('-data_prevista')
	return render(request, 'especialistas/seila.html', {'incidentes':incidentes})
	