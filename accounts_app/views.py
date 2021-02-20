from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        pwd = request.POST['password']
        user1 = auth.authenticate(username=user, password=pwd)
        if user1 is not None:
            auth.login(request, user1)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'User name or password is not valid'})
    else:
        return render(request, 'account/login.html')


def signup(request):
    if request.method == 'POST':
        username1 = request.POST['user']
        pwd1 = request.POST['pass1']
        pwd2 = request.POST['pass2']
        if pwd1 == pwd2:
            try:
                User.objects.get(username=username1)
                return render(request, 'account/signup.html', {'error': 'user name hase been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username1, password=pwd1)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords are not same'})

    return render(request, 'account/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'account/signup.html')
