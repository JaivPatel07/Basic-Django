from django.shortcuts import render

# import things we initially we dont have urls.py in app so we need to create urls.py in app1.

# Create your views here.
def app1(request):
    return render(request,'app1.html')