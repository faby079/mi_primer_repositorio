from django.shortcuts import render

# Create your views here.
def  notas_page_view(request):
    return render(request,'notas.html')