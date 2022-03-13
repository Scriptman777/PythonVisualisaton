import pandas
import plotly.express as px

df = pandas.read_csv("Summary.csv")

fig = px.bar(df, x="Library", y=["Input", "Output", "Types", "Customisation", "Interactivity"], title="Summary", labels={'value': 'Score'}, color_discrete_sequence=px.colors.qualitative.G10)

fig.write_image("Summary.svg")
fig.show()
