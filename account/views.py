from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic import TemplateView

# from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.shortcuts import redirect


#%%
from account.forms import AccountCreationForm
from .validators import *
#%%
class Registration(View):

    def post(self, request):
        validators = [MinimumLengthValidator, NumberValidator, UppercaseValidator]
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
        logout(request)
        return redirect('landing')