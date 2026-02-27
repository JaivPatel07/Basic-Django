from django.shortcuts import render
from .models import Employee

# import things we initially we dont have urls.py in app so we need to create urls.py in app1.

# Create your views here.
def app1(request):
    temp = Employee.objects.all()
    return render(request,'app1.html',{'details':temp})