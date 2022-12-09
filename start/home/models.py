from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=188)
    age = models.PositiveIntegerField()


class Employee(models.Model):
    Emp_id=models.PositiveIntegerField()
    Emp_name=models.CharField(max_length=180)
    dept=models.CharField(max_length=50)

