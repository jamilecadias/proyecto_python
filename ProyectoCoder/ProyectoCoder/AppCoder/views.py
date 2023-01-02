from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso
from django.core import serializers

from AppCoder.forms import *  



# Create your views here.

def buscarcurso(request):
    return render(request, "AppCoder/buscarCurso.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request,"AppCoder/cursosEncontrados.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"],numero_dia=informacion["numero_dia"],)
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def cursosapi(request):
    cursos_todos = Curso.objects.all()
    print(cursos_todos)
    return HttpResponse(serializers.serialize('json',cursos_todos))

def profesores(request):
    return HttpResponse("Vista de profesores")


def leer_cursos(request):
    cursos = Curso.objects.all()
    #contexto = {"cursos":cursos}
    return HttpResponse(serializers.serialize('json',cursos))


def crear_curso(request):
    curso = Curso(nombre = 'TestIngresoCRUD',camada = 122, numero_dia=55)
    curso.save()
    return HttpResponse('Curso TestIngresoCRUD creado')


def actualizar_curso(request):
    nombre = 'TestIngresoCRUD'
    nombre_nuevo = 'NuevoTestIngresoCRUD'
    Curso.objects.filter(nombre=nombre).update(nombre=nombre_nuevo)
    return HttpResponse(f'Curso {nombre} actualizado')


def borrar_curso(request):
    nombre = 'NuevoTestIngresoCRUD'
    curso = Curso.objects.get(nombre=nombre)
    curso.delete()
    return HttpResponse(f'Curso {nombre} eliminado')

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView

class CursoCreacion(CreateView):
    model = Curso
    fields= '__all__'
    success_url= '/AppCoder/curso/list'

class CursoList(ListView):
    model = Curso
    template_name="AppCoder/cursos_list.html"


# Editar
class CursoEdit(UpdateView):
    model = Curso
    fields= '__all__'
    success_url= '/AppCoder/curso/list'  

from django.views.generic.detail import DetailView
# Detalle
class CursoDetail(DetailView):
    model = Curso
    template_name="AppCoder/cursos_detail.html"

# Borrar
class CursoDelete(DeleteView):
    model = Curso
    #fields= '__all__'
    success_url= '/AppCoder/curso/list'    