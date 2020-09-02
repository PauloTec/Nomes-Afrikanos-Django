from django.shortcuts import render, redirect
from . models import Nome
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def lista_nomes(request):
	#return render(request, 'nomes/lista_nomes.html')
	nomes = Nome.objects.all().order_by('nome') #buscar todos os produtos
	return render(request, 'nomes/lista_nomes.html', {'nome':nomes})

@login_required(login_url="/contas/login/") #obriga a buscar login antes de executar a função!
def criar_nome(request):
	if request.method == 'POST':
		form = forms.CriarNome(request.POST)
		if form.is_valid():
			#gravar na base de dados e redirecionar a lista de nomes atualizada
			instance = form.save(commit=False)
			instance.autor_nome = request.user #buscar usuario
			instance.save()
			return redirect('lista')
	else:
		form = forms.CriarNome()
		return render(request, 'nomes/cadastrar_nome.html', {'form':form})

def nome_detalhe(request, slug):
	return HttpResponse(slug)

