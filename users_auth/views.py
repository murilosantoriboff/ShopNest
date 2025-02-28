from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    elif request.method == 'POST':
        # Coletando as informações
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        users = User.objects.filter(username=nome)

        if users.exists():
            return redirect('/auth/registro/?erro=user_exists')

        if senha1 != senha2:
            return redirect('/auth/registro/?erro=different_passawords')

        if len(senha1) < 6:
            return redirect('/auth/registro/?erro=short_password')
        
        try:
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha1
            )
            return redirect('/auth/logar/')
        except:
            return redirect('/auth/registro/?erro=erro_unknown')

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=nome, password=senha)
        
        if user:
            auth.login(request, user)
            return redirect('/')
        return redirect('/auth/logar/?error=login_error')
    
@login_required(login_url='/auth/registro/')
def sair(request):
    auth.logout(request)
    return redirect('/auth/logar/?status=logout')