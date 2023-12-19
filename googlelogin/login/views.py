from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# @user_passes_test(lambda u: u.is_authenticated, login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def check_auth_view(request):
    # This view will only be accessible if the user is authenticated
    # You can perform additional checks or render specific content here
    return render(request, 'check_auth.html')  # Change 'check_auth.html' to your actual template

@cache_control(no_store=True, no_cache=True)
def home(request):
    return render(request,'Home.html')
def Logout(request):
    logout(request)
    return redirect('home')