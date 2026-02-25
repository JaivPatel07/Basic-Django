from django.http import HttpResponse

from django.shortcuts import render # render is a shortcut function that combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text. It is used to render HTML templates and return them as responses to HTTP requests.


def home(request):
    return HttpResponse("home page")  # it returns a simple HttpResponse with the text "home page" when the home view is accessed.

def about(request):
    # return HttpResponse("about page")
    return render(request, 'about.html')  # it renders the 'about.html' template and returns it as an HttpResponse when the about view is accessed.

    # it will show an error because we have not created the about.html file yet. so we need to create a templates folder in our core app and then create the about.html file inside that templates folder.

    # but things not over yet we need to tell Django where to look for the templates. so we need to add the templates folder to the TEMPLATES setting in the settings.py file. go to settings.py file and find the TEMPLATES setting and then add the path to the templates folder in the DIRS list. 



def contact(request):
    return HttpResponse("contact page")