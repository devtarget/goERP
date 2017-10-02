from django.shortcuts import render
from goerp.usuarios.models import Usuarios

# Create your views here.

def cadastrousuarios(request):
	modelo = Usuarios()
	if request.method == 'POST'	:
		modelo.login = request.POST.get('login','')
		modelo.nome = request.POST.get('nome','')
		modelo.senha = request.POST.get('senha','')
		modelo.salvar()
		return render(request, 'usuarios/cadastro.html')
	return render(request, 'usuarios/cadastro.html')

def listausuarios(request):
	usuario = Usuarios.objects.all()
	dados = {}
	dados['object_list'] = usuario
	return render(request, 'usuarios/lista.html', dados)