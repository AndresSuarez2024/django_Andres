from django.shortcuts import render, redirect
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm  # Asegúrate de tener forms.py


def index(request):
    return render(request, 'centre/index.html')


def students(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('students')  # Redirige a la lista de estudiantes

    return render(request, 'centre/students.html', {'students': students, 'form': form})


def teachers(request):
    teachers = Teacher.objects.all()
    form = TeacherForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('teachers')  # Redirige a la lista de profesores

    return render(request, 'centre/teachers.html', {'teachers': teachers, 'form': form})
