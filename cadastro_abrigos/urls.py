from django.conf.urls import url
from . import views

app_name = 'abrigos'

urlpatterns = [
	url(r'^$', views.indice, name='indice'),
]
