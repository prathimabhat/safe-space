from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import transaction

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    form=SignUpForm
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()

            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_normal_user=True
            user.profile.user_name=form.cleaned_data.get('username')
            user.profile.email_id=form.cleaned_data.get('email')
            user.profile.first_name=form.cleaned_data.get('first_name')
            user.profile.last_name=form.cleaned_data.get('last_name')
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.reason = form.cleaned_data.get('reason')
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')

