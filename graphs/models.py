
#%%
# Import libraries
import numpy as np
import pandas as pd
import datetime as dt
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.offline

from django.db import models

tls.set_credentials_file(username='matisa360', api_key='894cZ80Vo3pEqSxdW6mw')
#%%
# Create your models here.
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

    def createMap(self, choosen_col=1):
        data, layout = preprocessing(choosen_col)
        fig = dict(data=data, layout=layout)
        return plotly.offline.iplot(fig, include_plotlyjs=False, output_type='div')

    def __str__(self):
        return self.title_for_map
