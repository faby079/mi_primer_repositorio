"""recetas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from foods import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home_page_view ,name= 'home'),
    path('menus',views.menus_page_view,name ='menus'),
    path('pasta',views.pasta_page_view,name ='pasta'),
    path('spaguettis',views.spaguettis_page_view,name ='spaguettis'),
    path('rusa',views.rusa_page_view,name ='rusa'),
    path('frigol',views.frigol_page_view,name ='frigol'),
    path('gaz',views.gaz_page_view,name ='gaz'),
    path('guisado',views.guisado_page_view,name ='guisado'),
    path('masa',views.masa_page_view,name ='masa'),
    path('sopas',views.sopas_page_view,name ='sopas'),
    path('facil',views.facil_page_view,name ='facil'),
    path('lista',views.lista_page_view,name ='lista'),

]
