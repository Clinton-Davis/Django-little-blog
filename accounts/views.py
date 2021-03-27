from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from contact.models import Contact, Valuation


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
       # Check if paswords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already being used")
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    # LOGIN AFTER REGISTER
                    auth.login(request, user)
                    messages.success(
                        request, 'You are Registered and have been logged in.')
                    return redirect('/')
        else:
            messages.error(request, "Passwords don't match, try again")
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:  # user is fond
            auth.login(request, user)
            messages.success(
                request, 'You are Logged in. Welcome back')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('pages:index')

