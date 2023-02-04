from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Incorrect Credentials, Try Again..."))
            return redirect('login_user')
    
    else:
        return render(
            request,
            'authenticate/login_user.html',
            {}
        )


def logout_user(request):

    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')
