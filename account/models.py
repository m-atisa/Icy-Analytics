from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import validate_extension
#%%
import numpy as np
import pandas as pd
import datetime as dt
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.offline
tls.set_credentials_file(username='matisa360', api_key='894cZ80Vo3pEqSxdW6mw')
#%%


class AccountManager(BaseUserManager):
#  or not validate_email(email)
    # Must override create_user and create_superuser
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError("Users must have a valid email address")
        if not password:
            raise ValueError("Users must have a valid password")
        if not first_name:
            raise ValueError("Users must have a valid first_name")
        if not last_name:
            raise ValueError("Users must have a valid last_name")

        user = self.model(
            email=self.normalize_email(email),
            # password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email        = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password     = models.CharField(verbose_name="password", max_length=100)
    date_joined  = models.DateTimeField(verbose_name="date", auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name   = models.CharField(verbose_name="first name", max_length=60, unique=False)
    last_name    = models.CharField(verbose_name="last name", max_length=60, unique=False)
    institution  = models.CharField(verbose_name="School/Company", max_length=60, unique=False)

    objects = AccountManager()

    # Whatever you want the user to login in with
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name',]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class American_States(models.Model):

    csv_file = models.FileField()
    title_for_map = models.CharField(max_length=80)

    def preprocessing(self, choosen_col):
        states = pd.read_csv(self.csv_file_path)
        states['text'] = str(choosen_col) + states[choosen_col].astype(str) + '<br>' 
        data = [dict(type='choropleth', autocolorscale=False, locations=states['states'], 
                z=states[passed_col], locationmode='USA-states', text=states['text'], colorscale='custom-colorscale', colorbar=dict(title=choosen_col))]
        layout = dict(title=self.title_for_map, geo=dict(scope='usa', 
                projection=dict(type='albers usa'), showlakes=True, lakecolor='rgb(66,165,245)'))
        return data, layout

    def createMap(self, choosen_col, filename):
        data, layout = preprocessing(choosen_col)
        fig = dict(data=data, layout=layout)
        return plotly.offline.iplot(fig, include_plotlyjs=False, output_type='div')

    def __str__(self):
        return self.title_for_map

class ExcelDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=user_directory_path, validators=[validate_extension])

    def retrieve_data(request):
        # This query will yield you the files that are relevant to the specifc user.
        data = ExcelDocument.objects.filter(user=request.user.id)
        if data is None:
            return []
        else:
            return data
            
    

        
