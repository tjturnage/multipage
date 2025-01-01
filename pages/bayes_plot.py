"""

"""

import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input, callback
import plotly.graph_objects as go



dash.register_page(__name__,
    path='/bayes_plot',
    title='Bayes Theorem',
    name='Bayes Theorem',
    order=3)

print("setting up grid ...")
N = 50
Y = np.arange(0, 1.02, 0.02)
Z = np.arange(0, 1.02, 0.02)
y, z = np.meshgrid(Y, Z)

print("Success !")

def create_surface(prior):
    """
    Create a surface plot of the posterior probability.
    """
    post = (prior * y) / ((prior * y) + z * (1 - prior))
    prior_str = f'Prior Prob: {prior:.2f}'
    trace = go.Surface(
        x=y, y=z, z=post, colorscale='Viridis', opacity=0.35,
        contours=go.surface.Contours(
            x=go.surface.contours.X(highlight=False),
            y=go.surface.contours.Y(highlight=True, highlightcolor="#ff3333"),
            z=go.surface.contours.Z(highlight=False),
        ),
        hovertemplate=prior_str +
        '<br>Prob Hypothesis True: %{x:.2f}' +
        '<br>Prob Hypothesis Null: %{y:.2f}' +
        '<br>New Posterior Prob: %{z:.2f}<extra></extra>'
    )
    return trace

layout = dbc.Container(html.Div([
    html.H1("Bayes' Theorem Calculation"),
    dbc.Label("Adjust the prior probability:"),
    dcc.Slider(
        id='prior-slider',
        min=0,
        max=1,
        step=0.05,
        value=0.4,
        marks={i: f'{i:.2f}' for i in np.arange(0, 1.05, 0.05)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    dcc.Graph(id='bayes-plot', style={'height': '800px'})  # Adjust the height here
]))

@callback(
    Output('bayes-plot', 'figure'),
    Input('prior-slider', 'value'),
)
def update_figure(prior):
    """
    Update the surface plot based on the prior probability.
    """
    trace = create_surface(prior)
    fig = go.Figure(data=[trace])
    fig.update_layout(
        title=f"Bayes' Theorem Calculation<br>Prior Probability = {prior:.2f}",
        # scene=dict(
        #     xaxis_title='Prob Hypothesis True',
        #     yaxis_title='Prob Hypothesis Null',
        #     zaxis_title='Posterior Probability'
        # ),
        scene={'xaxis_title': 'Prob Hypothesis True',
               'yaxis_title': 'Prob Hypothesis Null',
               'zaxis_title': 'Posterior Probability'},
        #margin=dict(l=0, r=0, b=0, t=40),
        margin={'l':0, 'r':0, 'b':0, 't':40},
        height=800  # Adjust the height here
    )
    #camera = dict(eye=dict(x=1.12, y=1.8, z=0.75))
    camera = {'eye':{'x':1.12, 'y':1.8, 'z':0.75}}

    fig.update_layout(scene_camera=camera)
    return fig
