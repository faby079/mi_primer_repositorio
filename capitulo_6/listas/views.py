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
    prioridad = request.GET.get('get_prioridad', default='%')
    with open("debug.log","w") as debug_file:
        print(f"SELECT * FROM notas WHERE prioridad LIKE '{prioridad}';",file=debug_file)


        cursor.execute("SELECT * FROM notas WHERE prioridad LIKE %s",(prioridad))
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        params = {'notas': result}
        return render(request,'notas.html',params)













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









