
#%%
# Import libraries
import numpy as np
import pandas as pd
import datetime as dt
import chart_studio.plotly as py
import chart_studio.tools as tls
#%%
from plotly.offline import plot
from plotly.graph_objs import Scatter

from django.db import models

from django.views.generic.base import TemplateView

tls.set_credentials_file(username='matisa360', api_key='894cZ80Vo3pEqSxdW6mw')
#%%
# Create your models here.

def AmericanStates(csv_file_path):
     x_data = [0,1,2,3]
     y_data = [x**2 for x in x_data]
     plot_div = plot([Scatter(x=x_data, y=y_data,
     mode='lines', name='test', opacity=0.8, marker_color='green')],
     output_type='div', include_plotlyjs=False, show_link=False, link_text="")
     return plot_div

def GetStateAbbreviations():
     state_abbreviations = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
     }
     return state_abbreviations
# states = pd.read_csv(csv_file_path) 
# choosen_col = states.iloc[:,0][1]
# states['text'] = str(choosen_col) + states[choosen_col].astype(str) + '<br>' 
# data = [dict(type='choropleth', autocolorscale=False, locations=states['State Names'], 
#           z=states[passed_col], locationmode='USA-states', text=states['text'], colorscale='custom-colorscale', colorbar=dict(title=choosen_col))]
# layout = dict(title=title_for_map, geo=dict(scope='usa', 
#           projection=dict(type='albers usa'), showlakes=True, lakecolor='rgb(66,165,245)'))
# fig = dict(data=data, layout=layout)
# return plot.iplot(fig, include_plotlyjs=False, output_type='div', show_link=False, link_text="")

    


# x_data = [0,1,2,3]
#      y_data = [x**2 for x in x_data]
#      plot_div = plot([Scatter(x=x_data, y=y_data,
#         mode='lines', name='test', opacity=0.8, marker_color='green')],
#         output_type='div', include_plotlyjs=False, show_link=False, link_text="")


