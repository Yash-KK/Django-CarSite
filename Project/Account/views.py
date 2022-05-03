from django.shortcuts import redirect, render

from .forms import CreateUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!')
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully!')
            return redirect('login')
    else:
        form = CreateUserForm()
            
    return render(request, 'Account/register.html',{
        "form":form
    })

@login_required(login_url='login') 
def user_dashboard(request):
    messages.success(request,'Logged In Successfully!')
    return render(request,'Account/dashboard.html')  