from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    render (request, 'blog/home.html')

#def about(request):
 #   return HttpResponse("<h1> This is an about page</h1>")