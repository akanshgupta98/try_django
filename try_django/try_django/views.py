from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth import authenticate
from blog.form import LoginForm


#TEMPLATES CONCEPT
def home_page(request):
    # page_title = 'Welcome to homepage'
    return render(request,"byte_blaze.html")

def login_page(request):
    
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print("USER IS AUTHENTICATED")
            ...
        else:
            print("USER IS NOT AUTHENTICATED")
            # No backend authenticated the credentials
            ...
    
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


