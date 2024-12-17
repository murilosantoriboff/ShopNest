from django.shortcuts import render

#TODO Trabalhar na autenticação (Verificacoes, login e rediricionamento) USAR DJANGO.CONTRIB.AUTH
def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    elif request.method == 'POST':
        pass

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')