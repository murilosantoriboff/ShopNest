from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse

#TODO Tarefas especificas usar login_required
@login_required(login_url='/auth/registro/')
def home(request):
    return render(request, 'home.html')

def perfil_usuario(request):
    #TODO Filtrar dados do usuario e mandar para a pagina de perfil
    return render(request, 'perfil_user.html')