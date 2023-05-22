from django.shortcuts import render

# Create your views here.
from .models import postProject

def project_post_page(request):
    article = postProject.objects.get(id=1)
    template_name = "project_page.html"
    context = {"object":article}
    return render(request, template_name, context)