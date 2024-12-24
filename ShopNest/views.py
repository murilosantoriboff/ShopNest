from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#TODO Tarefas especificas usar login_required
def home(request):
    return render(request, 'home.html')