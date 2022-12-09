from django.contrib import admin
from .models import *
from .models import Employee
# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)