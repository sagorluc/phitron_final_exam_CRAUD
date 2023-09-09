from django.shortcuts import render, redirect
from accounts_app.forms import RegistrationFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = RegistrationFrom()
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationFrom()
    return render(request, 'register.html', {'forms': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Loged in successfully')
            return redirect('show_crud')
        else:
            messages.error(request, 'User not found')
            return redirect('login')
              
    return render(request, 'login.html')

@login_required
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Loged in successfully.')
    return redirect('login')