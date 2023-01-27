import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from .side_bar import sidebar
import pandas as pd
from pathlib import Path

#p = Path('/home/tjturnage')
p = Path('C:/data/scripts')


q = p / 'multipage' / 'assets' / 'Berlin_crimes.csv'

if q.exists():
    data = q
else:
    data = "assets/Berlin_crimes.csv"

df = pd.read_csv(data)

#print(df)

dash.register_page(__name__, title="Grafitti", order=1)





def layout():
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
                                id="district_chosen",
                                options=df["District"].unique(),
                                value=["Lichtenberg", "Pankow", "Spandau"],
                                multi=True,
                                style={"color": "black"},
                            ),
                            html.Hr(),
                            dcc.Graph(id="line_chart", figure={}),
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


@callback(Output("line_chart", "figure"), Input("district_chosen", "value"))
def update_graph_card(districts):
    if len(districts) == 0:
        return dash.no_update
    else:
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
