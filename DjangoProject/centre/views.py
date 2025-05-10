from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm

def index(request):
    return render(request, 'centre/index.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'centre/students.html', {'students': students})

def students_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'centre/students_detail.html', {'student': student})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'centre/teachers.html', {'teachers': teachers})

def teachers_detail(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    return render(request, 'centre/teachers_detail.html', {'teacher': teacher})

def add_students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirige a la lista de estudiantes después de agregar
    else:
        form = StudentForm()
    return render(request, 'centre/add_students.html', {'form': form})

def add_teachers(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')  # Redirige a la lista de profesores después de agregar
    else:
        form = TeacherForm()
    return render(request, 'centre/add_teachers.html', {'form': form})
