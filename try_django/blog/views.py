from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogPost
from django.http import Http404
from blog.form import BlogPostForm, BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

# @login_required(login_url='/login')
@staff_member_required
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

@staff_member_required
def blog_post_update_view(request,post_slug):
    obj = get_object_or_404(BlogPost,slug=post_slug)
    # qs = BlogPost.objects.filter(slug=post_slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
        print("Data is updated")
    
    context = {"objects":obj,"forms":form}
    return render(request,"blog/update.html",context)

@staff_member_required
def blog_post_delete_view(request,post_slug):

    obj = get_object_or_404(BlogPost,slug = post_slug)

    if request.method == "POST":
        obj.delete()
        return redirect("/blogs")
    
    context = {"object":obj}

    return render(request,"blog/delete.html",context)