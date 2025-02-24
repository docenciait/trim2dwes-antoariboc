from django.shortcuts import render, redirect
from .forms import DenunciaForm
from .models import Denuncia
# Create your views here.

def lista_denuncias(request):
    
    template_data = {}
    template_data['title'] = 'Denuncias'
    template_data['denuncias'] = Denuncia.objects.all()
    return render(request, 'denuncias/lista_denuncias.html',{'template_data': template_data})
    

def crear_denuncia(request):
    
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = DenunciaForm()
        return render(request, 'denuncias/crear_denuncia.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('denuncias.denuncia')
        else:
            template_data['form'] = form
            return render(request, 'denuncias/crear_denuncia.html',{'template_data': template_data})

def editar_denuncia(request):
    pass

def eliminar_denuncia(request):
    pass
