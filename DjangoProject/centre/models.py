from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name1 = models.CharField(max_length=100)
    last_name2 = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    modules = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name1}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name1 = models.CharField(max_length=100)
    last_name2 = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.TextField()
    tutor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name1}"
