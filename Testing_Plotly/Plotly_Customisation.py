import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,500)
smooth_y = np.sin(smooth_x)

random_x = np.linspace(0,100,50)
random_y = np.random.randint(50, size=50)

# Experiments


fig = make_subplots(rows=3, cols=1, subplot_titles=("Bar chart", "Line chart", "Scatter chart"))


fig.add_trace(
    go.Bar(x=cats, y=data, marker_color=['red','yellow','cyan','blue','green','lime'], text=data), 
    row=1, col=1
)


fig.add_trace(
    go.Scatter(x=smooth_x, y=smooth_y, line=dict(color='red', width=4, dash='dash')),
    row=2, col=1
)


fig.add_trace(
    go.Scatter(x=random_x, y=random_y, mode='markers', marker=dict(size=random_y, cmax=50, cmin=0, color=random_y, colorscale="Thermal")),
    row=3, col=1
)




fig.update_layout(showlegend=False, width=1200, height=2000)
fig.show()