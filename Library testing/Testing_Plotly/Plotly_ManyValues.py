import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


fig = make_subplots(rows=3, cols=1, subplot_titles=("Line plot", "Scatter plot", "Bar plot"))


# Sample data

data = pd.read_csv('MOCK_DATA.csv')

x = np.linspace(0,2*np.pi,50)
sin_x = np.sin(x)
cos_x = np.cos(x)
sin_2x = np.sin(2*x)
cos_x_2 = np.cos(x)*2
sqrt_x = np.sqrt(x)

# Line plot

fig.add_trace(
    go.Scatter(x=x, y=sin_x),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=cos_x, line=dict(color='red', width=4, dash='dash')),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=sin_2x, line=dict(color='green', width=4, dash='dot')),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=cos_x_2, line=dict(color='blue', width=4, dash='longdash')),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=sqrt_x, line=dict(color='purple', width=4, dash='dashdot')),
    row=1, col=1
)

# Scatter plot

fig.add_trace(
    go.Scatter(x=x, y=sin_x, mode='markers'),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=cos_x, mode='markers', marker=dict(color='red', symbol='diamond')),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=sin_2x, mode='markers', marker=dict(color='green', symbol='star', size=10)),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=cos_x_2, mode='markers', marker=dict(color='blue', symbol='hexagram')),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=x, y=sqrt_x, mode='markers', marker=dict(color='purple', symbol='triangle-sw-dot')),
    row=2, col=1
)

# Bar plot


def AssignColor(cat):
    if cat == 'A':
        return 'red'
    elif cat == 'B':
        return 'blue'
    elif cat == 'C':
        return 'green'
    elif cat == 'D':
        return 'yellow'
    elif cat == 'E':
        return 'orange'
    return 'black'


fig.add_trace(
    go.Bar(x=data['company'], y=data['profit'], text=data['exchange'], marker=dict(color = list(map(AssignColor, data['arbitraryCategory'])))),
    row=3, col=1
)



fig.update_layout(showlegend=False, width=1200, height=2000)
fig.show()