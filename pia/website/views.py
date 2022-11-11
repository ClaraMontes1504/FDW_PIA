from django.shortcuts import render

from .models  import Sucursal

# Create your views here.
def index(request):
    sucursales = Sucursal.objects.all()
    context = {
        "sucursales" : sucursales
    }
    return render(request, 'index.html', context)

