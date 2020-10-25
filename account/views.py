from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from account.forms  import AccountCreationForm

class Registration(View):

    def post(self, request):
        context = {}
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('landing')
