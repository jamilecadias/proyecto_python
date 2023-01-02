from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path("cursos/", views.cursos,name='Cursos'),
    path("cursosApi/", views.cursosapi),
    path("profesores/", views.profesores),
    path("buscarCurso/", views.buscarcurso,name='Buscar'),
    path("buscar/", views.buscar),
    path("leerCursos/", views.leer_cursos),
    path("crearCurso/", views.crear_curso),
    path("actualizarCurso/", views.actualizar_curso),
    path("borrarCurso/", views.borrar_curso),
    path("curso/create/",views.CursoCreacion.as_view(),name='New'),
    path("curso/list/",views.CursoList.as_view(),name='List'),
    path("curso/edit/<pk>",views.CursoEdit.as_view(),name='Edit'),
    path("curso/detail/<pk>",views.CursoDetail.as_view(),name='Detail'),
    path("curso/delete/<pk>",views.CursoDelete.as_view(),name='Delete'),
]
