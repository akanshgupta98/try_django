from django.shortcuts import render
from .models import BlogPost
from django.http import Http404

# Create your views here.

def blog_post_page(request,slug=None):
    if slug == None:
        context = BlogPost.objects.all
        print(type(context))
    else:
        querySet = BlogPost.objects.filter(slug=slug)
        print(type(querySet))
        if querySet.count() < 1:
            raise Http404
        # if type(context) != list:
        #     context_temp = []
        #     context_temp.append(context)
        #     context = context_temp
    
    # print("context is; ",context)

    return render(request, 'blog_post.html',{"posts":querySet})