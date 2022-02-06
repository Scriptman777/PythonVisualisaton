import pandas as pd
import numpy as np
import plotly.express as px

# Sample data

data = pd.read_csv('MOCK_DATA.csv')

# Bar plot

fig = px.bar(data, x='company', y='profit', color='arbitraryCategory', text='exchange')
fig.show()