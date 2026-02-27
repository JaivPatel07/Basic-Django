from django.contrib import admin
from .models import Employee # we need to import the Employee model to register it in the admin panel so that we can see the Employee model in the admin panel and we can also add, edit and delete the employee records from the admin panel.  
# Register your models here.

admin.site.register(Employee) # we need to register the Employee model in the admin panel so that we can see the Employee model in the admin panel and we can also add, edit and delete the employee records from the admin panel.