from django.shortcuts import render
from weather.models import Cidade

def index(request):
    cidades = Cidade.objects.all()
    return render(request, "weather/index.html", {"cidades": cidades})
# Create your views here

