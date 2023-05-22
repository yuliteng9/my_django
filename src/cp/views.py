from django.shortcuts import render
from .models import ProjectPost

# Create your views here.
def project_post_page(request, post_id=1):
    obj = ProjectPost.objects.get(id=post_id)
    template_name = "project_post_page.html"
    context = {"h1": "Project Post", "project": obj}
    return render(request, template_name, context)