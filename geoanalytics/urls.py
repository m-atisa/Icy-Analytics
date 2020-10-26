"""geoanalytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
#%%
from account.views import (
    Registration, LogOut
)
#%%
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'), # Don't know why but this is needed
    path('register/', Registration.as_view()),
    path('logout/', LogOut.as_view(), name='logout'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('documentation/', TemplateView.as_view(template_name='documentation.html'), name='documentation'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)