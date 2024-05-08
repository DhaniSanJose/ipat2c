from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})



def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')


def add_record(request):
    forms = AddRecordForm(request.POST or None)
    if  request.user.is_authenticated:
        if request.method == 'POST':
            add_record = forms.save()
            messages.success(request, "Record Added...")
            return redirect('home')
        return render(request, "add_record.html", {'forms':forms})
    else:
         messages.success(request, "You Must Be Logged In...")
         return redirect('home')
    

def update_record(request, pk):
    if  request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record )
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated...")
            return redirect('home')
        return render(request, "update_record.html", {'form':form})

    else:
         messages.success(request, "You Must Be Logged In...")
         return redirect('home')    

def delete_record(request, pk):
    if  request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Has Been Deleted...")
        return redirect('home')

    else:
         messages.success(request, "You Must Be Logged In...")
         return redirect('home')   
