import psycopg2
from django.http import HttpResponse

from django.shortcuts import render
import psycopg2.extras
from django.http import HttpResponse
from django .shortcuts import redirect
# Create your views here.
def  notas_page_view(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="banana")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM notas;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'notas.html', params)


def insert (request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    contenido = request.POST["name_contenido"]
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="banana")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO notas VALUES ('{prioridad}','{titulo}','{contenido}');")

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('notas')









