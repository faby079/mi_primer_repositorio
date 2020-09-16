from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'recetas.html')


def menus_page_view(request):
    return render(request, 'menu_infantil.html')

def pasta_page_view(request):
    return render(request, 'canelones.html')


def spaguettis_page_view(request):
    return render(request, 'carbonara.html')


def rusa_page_view(request):
    return render(request, 'ensaladilla_rusa.html')


def frigol_page_view(request):
    return render(request, 'feijoada.html')


def gaz_page_view(request):
    return render(request, 'gazpacho.html')


def guisado_page_view(request):
    return render(request, 'mafe.html')


def masa_page_view(request):
    return render(request, 'pizza.html')


def sopas_page_view(request):
    return render(request, 'sopa_de_noodles.html')


def facil_page_view(request):
    return render(request, 'receta_facil.html')


def lista_page_view(request):
    return render(request, 'lista_recetas.html')







