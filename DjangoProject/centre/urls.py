from django.urls import path
from .views import index, students, teachers, add_students, add_teachers, students_detail, teachers_detail

urlpatterns = [
    path('', index, name='index'),
    path('students/', students, name='students'),
    path('students/<int:id>/', students_detail, name='students_detail'),
    path('teachers/', teachers, name='teachers'),
    path('teachers/<int:id>/', teachers_detail, name='teachers_detail'),
    path('students/add/', add_students, name='add_students'),
    path('teachers/add/', add_teachers, name='add_teachers'),
]
