from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Primer vista</h1>")


def nosotros(request):
    return HttpResponse("<h1>Nosotros</h1>")