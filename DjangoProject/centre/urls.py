from django.urls import path
from .views import index, students, teachers, add_students, add_teachers

urlpatterns = [
    path('', index, name='index'),
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('students/add/', add_students, name='add_students'),
    path('teachers/add/', add_teachers, name='add_teachers'),
]
