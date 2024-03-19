from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from home.forms import LoginForm, RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . utils import prbac_required






@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')



@prbac_required('route_1')
def route1(request):
    return render(request, 'route1.html')

@prbac_required('route_2')
def route2(request):
    return render(request, 'route2.html')

# authentication

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('account created successfully')
            return redirect('login')
        else:
            print('register failed')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')





