from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import ProjectPost

# Create your views here.
def project_page(request, post_id):
    try:
        project_obj = get_object_or_404(ProjectPost, id=post_id)
    except:
        raise Http404
    context= {'h1': "Project Post", "project" : project_obj }
    return render(request, "home_page.html", context)