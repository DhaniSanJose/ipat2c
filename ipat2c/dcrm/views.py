from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
# Create your views here.

def home(request):
    #DO SOMETHING

    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
             messages.success(request, "There was an Error Logging In, Please Try Again")
             return redirect('home')
    else:

        return render(request, 'home.html', {'records':records})





def register(request):

    return render(request, 'register.html')





def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')