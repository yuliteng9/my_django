from django.shortcuts import render

# Create your views here.
from .models import BlogPost
from .models import Comment

def blog_post_detail_page(request, post_id=1):
    blog_post = BlogPost.objects.get(id=post_id) # query -> database -> data -> django render it
    comments = []
    for _ in range(3, 5):
        comments.append(Comment.objects.get(id=_))  # query -> database -> data -> django render it
    template_name = "blog_post_detail.html"
    context = {"article":blog_post, "comments_list":comments}
    return render(request, template_name, context)
