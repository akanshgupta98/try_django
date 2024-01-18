from django.http import HttpResponse
from django.shortcuts import render


#TEMPLATES CONCEPT
def home_page(request):
    return render(request,"home_page.html")

#OKAY FOR A VERY SMALL EXAMPLE. 
def about_page(request):
    return HttpResponse("<h1>About Us</h1>")

def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")
