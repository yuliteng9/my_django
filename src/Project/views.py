from django.shortcuts import render

# Create your views here.
from .models import postProject

def project_post_page(request, post_id=1):
    article = postProject.objects.get(id=post_id)
    template_name = "project_page.html"
    context = {"object":article}
    return render(request, template_name, context)