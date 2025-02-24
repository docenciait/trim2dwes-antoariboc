from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.

def registro(request):    
    template_data = {}
    template_data['title'] = 'Registro'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'usuarios/registro.html', {'template_data': template_data})

def iniciar_sesion(request):
    pass

def cerrar_sesion(request):
    pass