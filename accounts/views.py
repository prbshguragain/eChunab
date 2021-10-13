from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request,user)
            return redirect('accounts:login')

    else:
        form = UserForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            return redirect('dashboard:dash')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):

    # Form POST banako bela ra yo jhan secure method ho #
    # if request.method == 'POST': #
    #     logout(request) #
    #     return redirect('landing_page') #

    logout(request)
    return redirect('landing_page')