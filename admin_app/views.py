from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Dashboard view
def admin_dashboard(request):
    return render(request, 'admin_app/admin_dashboard.html')

# Login page view
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'admin_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_app/login.html')

# Signup page view
def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'admin_app/signup.html', {'form': form})
