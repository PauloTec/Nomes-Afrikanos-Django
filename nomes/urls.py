from django.conf.urls import url
from . import views

#app_name='nomes'

urlpatterns = [
	url(r'^$', views.lista_nomes, name="lista"),
	url(r'^create/$', views.criar_nome, name="criar"),
	url(r'^(?P<slug>[\w-]+)/$', views.nome_detalhe, name="detalhe"),
]