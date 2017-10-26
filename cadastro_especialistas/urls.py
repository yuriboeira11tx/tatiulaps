from django.conf.urls import url
from . import views

app_name = 'especialistas'

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^cadastro/$', views.cadastro, name='cadastro'),
	url(r'^indice/$', views.indice, name='indice'),
]
