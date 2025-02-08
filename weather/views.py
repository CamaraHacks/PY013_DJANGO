from django.shortcuts import render, get_object_or_404
from weather.models import Cidade
from weather.utils import get_weather 

def index(request):
    cidades = Cidade.objects.all()
    return render(request, "weather/index.html", {"cidades": cidades})
# Create your views here

def previsao(request, pk):
    cidade = get_object_or_404(Cidade, pk=pk)
    prev = get_weather(cidade.lat, cidade.long)
    return render(
        request, 
        "weather/previsao.html", 
        {
         "cidade":cidade,
         "previsao": prev

         })