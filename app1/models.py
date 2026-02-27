from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    image = models.ImageField(upload_to='employee_images/') # here we need to specify the upload_to parameter to define the directory where the images will be stored
    date_added = models.DateTimeField(default=timezone.now)
    choice = [
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
    ]
    department = models.CharField(max_length=50, choices=choice)

    def __str__(self):
        return self.name
    
# things not over yet we need to tell django fro that we need to create migrations and then we need to migrate the database to create the table for the Employee model in the database. so that we can use the Employee model to create, read, update and delete the employee records in the database. and also we need to register the Employee model in the admin.py file so that we can see the Employee model in the admin panel and we can also add, edit and delete the employee records from the admin panel. so go to admin.py file and register the Employee model there.