#bayes_plot.py

import numpy as np
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Output, Input, no_update
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

print("setting up grid ...")
N = 50
Y = np.arange(0,1.02,0.02)
Z = np.arange(0,1.02,0.02)
y,z = np.meshgrid(Y,Z)

print("Success !")

prior = 0.4 # prior_probability
prior_str = f'Prior Prob: {prior:.2f}'
title_str = f"Bayes' Theorem Calculation<br>Prior Probability = {prior:.2f}"

post = (prior*y)/((prior*y) + z*(1 - prior))

trace = go.Surface(x=y,y=z,z=post, colorscale='Viridis', opacity=0.35, contours=go.surface.Contours(
        x=go.surface.contours.X(highlight=False),
        y=go.surface.contours.Y(highlight=True,highlightcolor="#ff3333"),
        z=go.surface.contours.Z(highlight=False),
        ),
        hovertemplate = prior_str +\
        '<br>Prob Hypothesis True: %{x:.2f}' +\
        '<br>Prob Hypothesis Null: %{y:.2f}' +\
        '<br>New Posterior Prob: %{z:.2f}<extra></extra>'
        )

data = [trace]
layout = go.Layout(title=title_str, autosize=False, width=900, height=800, margin=dict(l=65, r=50, b=65, t=90),
        scene=go.layout.Scene(
        xaxis = go.layout.scene.XAxis(showspikes=False),
        yaxis = go.layout.scene.YAxis(showspikes=False),
        zaxis = go.layout.scene.ZAxis(showspikes=True),
        )
        )

fig = go.Figure(data=data, layout=layout)

camera = dict(
    eye=dict(x=-1.2, y=-1.8, z=0.3)
)

fig.update_layout(scene_camera=camera,
                  scene = dict(
                    xaxis_title='Prob Hypothesis True',
                    yaxis_title='Prob Hypothesis Null',
                    zaxis_title='New Posterior Prob'),
                    hoverlabel_align = 'right',
)

app = Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server()