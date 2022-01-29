import numpy as np
import plotly.express as px

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig = px.bar(x=cats, y=data, title="Export test")


# Export

# requires kaleido library

fig.write_image("graph.png")
fig.write_image("graph.jpeg")
fig.write_image("graph.webp")
fig.write_image("graph.svg")
fig.write_image("graph.pdf")