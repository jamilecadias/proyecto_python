from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cursos(request):
    return HttpResponse('Vista de cursos')

def profesores(request):
    return HttpResponse('Vista de profesores')