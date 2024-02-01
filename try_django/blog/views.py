from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogPost
from django.http import Http404,HttpResponseForbidden
from blog.form import BlogPostForm, BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

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
    # print(form.is_valid())
    # print(request.user)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     form.user = request.user
    #     BlogPost.objects.create(**form.cleaned_data)
    #     form = BlogPostForm()

    form = BlogPostModelForm(request.POST or None)
    # print(form.cleaned_data)
    # print(request.POST['blog_title'])
    # print('post request data',request.POST)
    # if form is not None:
        # print('form fileds',form.fields)
        # print('form cleaned data',form.cleaned_data)
    # if request.method == "POST":
    #     BlogPost.objects.create(**request.POST)
    #     print(request.POST['blog_title'])
    
    
        # print(form.cleaned_data)

    if form.is_valid():
        print('cleaned data',form.cleaned_data)
        form_mod = form.save(commit=False)
        form_mod.user = request.user
        # form.fields.update({"publish_date":timezone.now()})
        
        if form.cleaned_data['action'] == "publish":
            # print("PUBLISHING",form.fields.publish_date)
            # form_mod.cleaned_data['publish_date'] = timezone.now()
            form_mod.publish_date = timezone.now()
            # form_mod.cleaned_data['content'] = 'fixed content'
            # form.publish_date = timezone.now()

        print('cleaned data before save',form.cleaned_data)
        form_mod.save()

        form = BlogPostModelForm()
    elif not form.is_valid() and form != None:
        print('form error: ',form.errors)

    context = {"form":form}
    return render(request,"blog/blog_create.html",context)

def blog_post_list_view(request):
    # BOTH CAN BE USED NOW. 
    # qs = BlogPost.objects.published()
    qs = BlogPost.objects.all().published()

    if request.user.is_authenticated:
        my_qs = BlogPost.objects.all()
        qs = (qs | my_qs).distinct()
    context = {"objects":qs}

    # print(str(qs[0].content)[:50])

    # return render(request,"blog/list.html",context)
    return render(request,"blog_list.html",context)

def blog_post_retrieve_view(request,post_slug):
    qs = BlogPost.objects.filter(slug=post_slug)
    context = {"objects":qs}
    return render(request,"blog/blog_retrieve.html",context)

@staff_member_required
def blog_post_update_view(request,post_slug):
    obj = get_object_or_404(BlogPost,slug=post_slug)
    # qs = BlogPost.objects.filter(slug=post_slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form_mod = form.save(commit=False)
        form_mod.user = request.user
        # form.fields.update({"publish_date":timezone.now()})
        
        if form.cleaned_data['action'] == "publish":
            # print("PUBLISHING",form.fields.publish_date)
            # form_mod.cleaned_data['publish_date'] = timezone.now()
            form_mod.publish_date = timezone.now()
    
        form.save()
        form = BlogPostModelForm()
        print("Data is updated")
        return redirect(obj.get_list_blogs_url())
    else:
        print('form error:',form.errors)
    
    context = {"objects":obj,"forms":form}
    return render(request,"blog/blog_update.html",context)

@staff_member_required
def blog_post_delete_view(request,post_slug):

    obj = get_object_or_404(BlogPost,slug = post_slug)

    if request.method == "POST":
        obj.delete()
        return redirect("/blogs")
    
    context = {"object":obj}

    return render(request,"blog/delete.html",context)

@staff_member_required
def blog_post_publish_view(request,post_slug):

    obj = get_object_or_404(BlogPost,slug = post_slug)


    if request is not None and request.method == "POST":
        obj.publish_date = timezone.now()
        obj.save()
        return redirect("/blogs")

    raise Http404
