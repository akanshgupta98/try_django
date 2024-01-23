from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
from blog.form import BlogPostForm, BlogPostModelForm

# Create your views here.

# def blog_post_page(request,slug=None):
#     if slug == None:
#         context = BlogPost.objects.all()
#         print(type(context))
#     else:
#         querySet = BlogPost.objects.filter(slug=slug)
#         print(type(querySet))
#         if querySet.count() < 1:
#             raise Http404
#         # if type(context) != list:
#         #     context_temp = []
#         #     context_temp.append(context)
#         #     context = context_temp
    
#     # print("context is; ",context)

#     return render(request, 'blog_post.html',{"posts":querySet})

# CRUD -> CREATE, RETRIEVE, UPDATE, DELETE. 
# GET -> RETRIEVE/LIST
# POST -> CREATE, UPDATE, DELETE


def blog_post_create_view(request):
    # form = BlogPostForm(request.POST or None)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     BlogPost.objects.create(**form.cleaned_data)
    #     form = BlogPostForm()

    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = BlogPostModelForm()

    context = {"form":form}
    return render(request,"blog/create.html",context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    context = {"objects":qs}

    return render(request,"blog/list.html",context)

def blog_post_retrieve_view(request,post_slug):
    qs = BlogPost.objects.filter(slug=post_slug)
    context = {"objects":qs}
    return render(request,"blog/retrieve.html",context)

def blog_post_update_view(request):
    return render(request,"blog/update.html")

def blog_post_delete_view(request):
    return render(request,"blog/delete.html")