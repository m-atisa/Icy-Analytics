from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.views.generic import TemplateView

# from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test

#%%
from account.forms import AccountCreationForm, AccountAuthenticationForm
#%%
class Registration(View):

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('landing')

        context = {}
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('landing')
        else:
            context['registration_form'] = form
        return render(request, 'register.html', context)
    
    def get(self, request):
        form = AccountCreationForm()
        context = {}
        context['registration_form'] = form
        return render(request, 'register.html', context)

class LogOut(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('landing')
        else:
            return redirect('landing')

class LogIn(View):

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('landing')
        context = {}
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('landing')
        context['signin_form'] = form
        return render(request, 'signin.html', context)
    
    def get(self, request):
        form = AccountAuthenticationForm()
        context = {}
        context['signin_form'] = form
        return render(request, 'signin.html', context)
