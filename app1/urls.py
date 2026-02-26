# things not over yet we we need to connect urls.py of app1 to the urls.py of project so that we can access the views of app1 from the urls of project. so go to core/urls.py and add the path for app1 urls.py there. also import include from django.urls to include the urls of app1 in the urls of project.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1, name='app1'),  # its home page of app1 when we go to app1/ it will render the app1.html template which we will create in templates folder of app1. so now go to app1/templates/app1.html and create a simple html file there.
]