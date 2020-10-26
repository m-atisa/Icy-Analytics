from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

# from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test


#%%
from account.forms import AccountCreationForm, AccountAuthenticationForm, ExcelForm
from account.models import ExcelDocument
#%%
class FileUploadView(CreateView):
    def post(self, request):
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = ExcelDocument(user=request.user, upload=request.FILES['upload'])
            newdoc.user = request.user
            newdoc.save()
            context = {}
            context['form'] = ExcelForm(request.FILES)
            context['documents'] = ExcelDocument.retrieve_data(request)
            return render(request, 'account/exceldocument_form.html', context)
    
    def get(self, request):
        context = {}
        context['form'] = ExcelForm(request.FILES)
        context['documents'] = ExcelDocument.retrieve_data(request)
        return render(request, 'account/exceldocument_form.html', context)

# class FileUploadView(ContextMixin, View):

#     model = ExcelDocument
#     fields = ['upload',]
#     success_url = reverse_lazy('fileupload')

#     def get_documents(self):
#         newdoc = ExcelDocument(user=self.request.user, upload=self.request.FILES['upload'])
#         newdoc.user = self.request.user
#         return newdoc

#     def get_context_data(self, **kwargs):
#         context = super(FileUploadView, self).get_context_data(**kwargs)
#         context['documents'] = ExcelDocument.objects.all()
#         return context
    
#     def get(self, **kwargs):
#         return get_context_data(self, **kwargs)

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
