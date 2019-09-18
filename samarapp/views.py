from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'samarapp/index.html')

def samar(request):
    return render(request,'samarapp/samar.html')
