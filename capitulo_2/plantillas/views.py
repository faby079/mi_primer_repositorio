

from django.shortcuts import render
# Create your views here.

def home_page_view(request):
    return render(request,'hola_mundo.html')



import random
def about_page_view(request):
   parametros = {'numero_favorito': random.randrange(10)}
   return render(request,'fabiola.html',parametros)


def send_page_view(request):
    return render(request,'azul_cielo.html')



