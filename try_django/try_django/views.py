from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


#TEMPLATES CONCEPT
def home_page(request):
    page_title = 'Welcome to homepage'
    return render(request,"home.html",{"title":page_title})

def login_page(request):
    if request.user.is_authenticated:
        return render(request,"login.html",{"title":"User Login Page","my_list":[1,2,3,4,5]})
    else:
        return render(request,"login.html",{"title":"User Login Page"})
    

#OKAY FOR A VERY SMALL EXAMPLE. 
# def about_page(request):
#     return HttpResponse("<h1>About Us</h1>")

def about_page(request):
    return render(request,"about.html",{"title":"About Us"})


def contact_page(request):
    return render(request,"contact.html",{"title":"Contact"})

# YOU CAN RENDER ANYTHING. NOT JUST HTML. EXAMPLE:
def render_anyting(request):

    template_obj = get_template("emp.txt")
    return HttpResponse(template_obj.render())


