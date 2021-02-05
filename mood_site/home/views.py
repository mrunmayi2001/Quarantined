from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home/index.html')

def art(request):
    
    return render(request,'home/art.html')

def cooking(request):
    
    return render(request,'home/cooking.html')

def exercise(request):
    
    return render(request,'home/exercise.html')

def gaming(request):
    
    return render(request,'home/gaming.html')

def meme(request):
    
    return render(request,'home/meme.html')

def meow(request):
    
    return render(request,'home/meow.html')

def page2(request):
    
    return render(request,'home/page2.html')

def page3(request):
    
    return render(request,'home/page3.html')

def woof(request):

    return render(request,'home/woof.html')

