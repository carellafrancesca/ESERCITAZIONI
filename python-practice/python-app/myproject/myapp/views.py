from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def saluta(request):
    nome = request.POST.get('nome', '')
    risposta = {"messaggio": f"Ciao, {nome}! Benvenuto nel backend di Django."}
    return JsonResponse(risposta)