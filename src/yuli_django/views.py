# Model View Template (MVT)
from django.shortcuts import render
from django.template.loader import get_template

# One web view is one function in this views.py file.


def home_page(request):
    my_title = "My Home Page"
    context = {"h1": my_title, "title": "HOME", "button_text": "Home Button", "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home_page.html", context)


def about_page(request):
    context = {"h1": "About us", "title": "ABOUT"}
    return render(request, "about_page.html", context)


def contact_page(request):
    context = {"h1": "Contact us", "title": "CONTACT"}
    return render(request, "contact_page.html", context)


def example(request):
    context = {"text_file": get_template("Strings.txt").render(), "h1": "Example", "title": "EXAMPLE"}
    return render(request, "about_page.html", context)


def intro_page(request):
    context = {"h1": "Intro", "title": "Project"}
    return render(request, "intro_page.html", context)