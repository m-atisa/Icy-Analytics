import numpy as np
import pandas as pd
import datetime as dt
import chart_studio.plotly as py
import chart_studio.tools as tls

tls.set_credentials_file(username='matisa360', api_key='894cZ80Vo3pEqSxdW6mw')


states = pd.read_csv("../media/user_1/files/popultion.csv") 
choosen_col = states.iloc[:,0][1]
states['text'] = str(choosen_col) + states[choosen_col].astype(str) + '<br>' 
data = [dict(type='choropleth', autocolorscale=False, locations=states['State Names'], 
          z=states[passed_col], locationmode='USA-states', text=states['text'], colorscale='custom-colorscale', colorbar=dict(title=choosen_col))]
layout = dict(title=title_for_map, geo=dict(scope='usa', 
          projection=dict(type='albers usa'), showlakes=True, lakecolor='rgb(66,165,245)'))
fig = dict(data=data, layout=layout)
return plot.iplot(fig, include_plotlyjs=False, output_type='div', show_link=False, link_text="")