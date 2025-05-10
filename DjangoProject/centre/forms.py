from django import forms
from .models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name1', 'last_name2', 'email', 'courses', 'tutor']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name1', 'last_name2', 'email', 'course']
