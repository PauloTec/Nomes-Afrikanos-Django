from django.http import HttpResponse
from django.shortcuts import render

#Função que retorna a página inicial
def index(request):
	return render(request, 'index.html')
	#return HttpResponse('Index')
def sobre(request):
	return render(request, 'sobre.html')

def contacto(request):
	return HttpResponse('Contacto')