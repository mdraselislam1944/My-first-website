from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentForm
from .forms import EmployeeForm
from .models import Student
from.models import Employee
from django.template import loader
from django.urls import reverse


def index(request):

    return render(request, 'home.html')


def CreateStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
       form = StudentForm()
    context = {'form': form}
    return render (request, 'check.html', context)


def CreateEmployee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    else:
       form = EmployeeForm()
    context = {'form': form}
    return render (request, 'print.html', context)

def show(request):

    return render(request, 'view_file.html')

def table(request):
    form=EmployeeForm()
    employees = Employee.objects.all().order_by("-id")
    context = {'form':form, 'employee':employees}
    return render (request, 'detail.html',context)


def delete(request, id):
  emp = get_object_or_404(Employee,id = id)
  emp.delete()
  return redirect('/detail')


def update(request, id):
  
  employee=Employee.objects.get(Emp_id=id)
  template = loader.get_template('update.html')
  context={'employe':employee}
  return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    
    return redirect('/detail')
  

