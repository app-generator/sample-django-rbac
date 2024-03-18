from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from home.forms import LoginForm, RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

def is_route1(user):
    return user.has_perm('app.can_access_route1')

def is_route2(user):
    return user.has_perm('app.can_access_route2')

@permission_required('app.can_access_route1', raise_exception=True)
def route1(request):
    # Assign users to group1
    users = User.objects.filter(username__in=['user_1', 'user_2'])
    group1 = Group.objects.get(name='group1')
    for user in users:
        user.groups.add(group1)

    return render(request, 'route1.html')

@permission_required('app.can_access_route2', raise_exception=True)
def route2(request):
    # Assign users to group2
    users = User.objects.filter(username__in=['user_3', 'user_4'])
    group2 = Group.objects.get(name='group2')
    for user in users:
        user.groups.add(group2)

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








# from django.http import HttpResponse
# from datetime import datetime
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import user_passes_test
# from .models import *
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import logout
# from home.forms import LoginForm, RegistrationForm
# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
# def index(request):

#     return render(request, 'index.html')




# def is_route1(user):
#     return user.groups.filter(name='group1').exists()

# def is_route2(user):
#     return user.groups.filter(name='group2').exists()

# @user_passes_test(is_route1)
# def route1(request):
   
#     return render(request, 'route1.html')

# @user_passes_test(is_route2)
# def route2(request):
   
#     return render(request, 'route2.html')


# #authentication

# class UserLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     form_class = LoginForm

#     def get_success_url(self):
#         return reverse_lazy('index')

# def register(request):
#     if request.method == 'POST':
#         form =  RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print('account created successfully')
#             return redirect ('login')
#         else:
#             print('register failed')
#     else:
#         form = RegistrationForm()

#     context = {
#         'form': form
#     }               

#     return render(request, 'accounts/register.html', context)

# def logout_view(request):
#     logout(request)
#     return redirect('login')