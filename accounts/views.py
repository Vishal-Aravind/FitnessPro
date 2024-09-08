#accounts/views.py

from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            print(f"User logged in: {user}")
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    else:
          if request.user.is_authenticated:
            return redirect('home')

    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')