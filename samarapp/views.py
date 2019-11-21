from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def samar(request):
    return render(request,'samar.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def about(request):
    return render(request,'about.html')
def games(request):
    return render(request,'games.html')
def gallery(request):
    return render(request,'gallery.html')
def sponsers(request):
    return render(request,'sponsers.html')
def team(request):
    return render(request,'team.html')
