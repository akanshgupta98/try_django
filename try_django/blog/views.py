from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def blog_post_page(request):
    context = BlogPost.objects.all
    print("context is; ",context)

    return render(request, 'blog_post.html',{"posts":context})