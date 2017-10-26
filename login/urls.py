from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
	url(r'^$', views.fazer_login, name='login'),
	url(r'^auth', views.direcionar, name='direcionar'),
	url(r'^logout', views.fazer_logout, name='logout'),
]
