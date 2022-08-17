from django.shortcuts import render
from django.http import HttpResponse
from employeeApp import views
from employeeApp.models import Employee
# Create your views here.
def index(request):
    return render(request, 'empApp/index.html')
def empview(request):
    emp_list = Employee.objects.all()
    my_dict ={'emp_list': emp_list}
    return render(request, 'empApp/employeeApp.html', context=my_dict)
