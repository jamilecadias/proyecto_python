from django.urls import path
from AppCoder import views

urlpatterns = [
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
]
