from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #para cadastro
from django.contrib.auth.forms import AuthenticationForm #para login
from django.contrib.auth import login, logout
 
# Create your views here.
def cadastro_view(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST) #se os dados forem do tipo POST
	
		if formulario.is_valid(): #se o form for válido
			user = formulario.save() #guardar os dados do usuario
			login(request, user)
			#logar usuario
			return redirect('lista') #ver ficheiro urls para obter nome do app e do link
	else: 
		formulario = UserCreationForm()
	return render(request, 'contas/cadastro.html',{'formulario':formulario})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			#entrar na pagina inicial do usuário
			#return render(request, 'kantina/index.html')
			return redirect('lista') 
	else:
		form = AuthenticationForm()

	return render(request, 'contas/login.html',{'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('nomes:lista')
