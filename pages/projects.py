"""
Main projects page is the graffitti page
"""
from pathlib import Path
import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
#from . import ids
from .side_bar import sidebar

GRAFFITI_LINE_CHART = "graf_line_chart"
DISTRICT_CHOSEN = "district_chosen"

p = Path('/home/tjturnage')
#p = Path('C:/data/scripts')


q = p / 'multipage' / 'data' / 'Berlin_crimes.csv'

if q.exists():
    DATA = q
else:
    DATA = "data/Berlin_crimes.csv"

df = pd.read_csv(DATA)

#print(df)

dash.register_page(__name__, title="Grafitti", order=1)

def layout():
    """
    Temp layout
    """
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col([sidebar()], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                    dbc.Col(
                        [
                            html.H3(
                                "Graffiti Incidents in Berlin",
                                style={"textAlign": "center"},
                            ),
                            dcc.Dropdown(
                                id = DISTRICT_CHOSEN,
                                options=df["District"].unique(),
                                value=["Lichtenberg", "Pankow", "Spandau"],
                                multi=True,
                                style={"color": "black"},
                            ),
                            html.Hr(),
                            dcc.Graph(id=GRAFFITI_LINE_CHART, figure={}),
                        ],
                        xs=8,
                        sm=8,
                        md=10,
                        lg=10,
                        xl=10,
                        xxl=10,
                    ),
                ]
            )
        ]
    )


@callback(Output(GRAFFITI_LINE_CHART, "figure"), Input(DISTRICT_CHOSEN, "value"))
def update_graph_card(districts):
    """
    Graffiti line chart
    """
    if len(districts) == 0:
        return dash.no_update

    df_filtered = df[df["District"].isin(districts)]
    df_filtered = (
        df_filtered.groupby(["Year", "District"])[["Graffiti"]]
        .median()
        .reset_index()
    )
    fig = px.line(
        df_filtered,
        x="Year",
        y="Graffiti",
        color="District",
        labels={"Graffiti": "Graffiti incidents (avg)"},
    ).update_traces(mode="lines+markers")
    return fig
