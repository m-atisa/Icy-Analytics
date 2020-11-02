#%%
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test

#%%
from account.forms import AccountCreationForm, AccountAuthenticationForm
from files.forms import ExcelForm
from files.models import ExcelDocument
from graphs.models import AmericanStates
#%%
import os
#%%
class InteractiveView(CreateView):

    """
    This method allows the user to upload a file 
    """
    def post(self, request):
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = ExcelDocument(user=request.user, upload=request.FILES['upload'])
            newdoc.user = request.user
            newdoc.save()
            context = {}
            context['form'] = ExcelForm(request.FILES)
            context['documents'] = ExcelDocument.retrieve_data(request)
            maps = []
            
            # Save the map to a file for later use
            f = open(str(newdoc) + ".html", "a")
            f.write(str(request.user) + "\maps\\" + AmericanStates(str(newdoc)))
            f.close()
            
            # Read in the html maps 
            user_maps = os.listdir(str(request.user) + "\maps\\")
            for map in user_maps:
                maps.append(open(map, "r").read())
            
            context['maps'] = maps
            return render(request, 'account/exceldocument_form.html', context)

    def get(self, request):
        context = {}
        context['form'] = ExcelForm(request.FILES)
        context['documents'] = ExcelDocument.retrieve_data(request)
        maps = []

        # Read in the html maps 
        user_maps = os.listdir(str(request.user) + "\maps\\")
        for map in user_maps:
            maps.append(open(map, "r").read())

        context['maps'] = maps
        return render(request, 'account/exceldocument_form.html', context)

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
