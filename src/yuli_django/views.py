# Model View Template (MVT)
from django.http import HttpResponse
from django.shortcuts import render

# One web view is one function in this views.py file.
def home_page(request):
    my_title = "My Home Page"
    return render(request, "home_page.html", {"h1":my_title, "title":"HOME"})

def about_page(request):
    return render(request, "about_page.html", {"h1":"About us", "title":"ABOUT"})

def contact_page(request):
    return render(request, "contact_page.html", {"h1":"Contact us", "title":"CONTACT"})

def example(request):
    return render(request, "home_page.html", {"h1":"example", "title":"EXAMPLE"})

def Project(request):
    return render(request, "project_page.html", {"h1":"Project Page", "title":"Project"})