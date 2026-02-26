"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # we need to import include to include the urls of app1 in the urls of project.

from . import views #importing the views.py file to use the functions we created there. (.) is used to import from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  #this is the home page we created in views.py
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


    path('app1/', include('app1.urls')), #when its go to app1/ that it can use app1.urls to find the views of app1 and render the templates of app1.
]
