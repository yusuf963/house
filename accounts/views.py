from django.shortcuts import (render, redirect)


def register(request):
    if request.method == 'POST':
        return redirect('register')
    return render(request, 'templates/accounts/register.html')


def login(request):
    if request.method == 'POST':
        return redirect('register')
    return render(request, 'templates/accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'templates/accounts/dashboard.html')
