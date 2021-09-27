import pandas as pd
import plotly.express as px

df = pd.read_csv('cars-iso.csv', dtype={"iso": str, 'production': int})

fig = px.choropleth(df, locations='iso', color='production', color_continuous_scale=px.colors.sequential.Plasma)
fig.write_html("Plotly output.html")