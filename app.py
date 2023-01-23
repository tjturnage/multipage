from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.DARKLY],use_pages=True)

assets_dir = "/home/tjturnage/multipage/assets"

top_content = [
            dbc.CardBody([html.H1("turnageweather", className="card-title",style={'font-weight': 'bold', 'font-style': 'italic'}),
                html.Div([
                dbc.CardLink("GitHub", href="https://github.com/tjturnage")]),
                html.Div([
                dbc.CardLink("@turnageweather", href="https://twitter.com/turnageweather")]),])
]
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Nav(
                        [
                            dbc.NavLink(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app")
                        ]
                    ),
                ]
            )
        ],
        fluid=True,
    ),dark=True,
    color="dark"
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == '__main__':
	app.run_server(debug=True)