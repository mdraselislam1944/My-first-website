from django import forms
from .models import *
from .models import Employee

class StudentForm(forms.ModelForm):
   class Meta:
      model = Student
      fields = "__all__"
class EmployeeForm(forms.ModelForm):
   class Meta:
      model = Employee
      fields = "__all__"

