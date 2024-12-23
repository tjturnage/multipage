"""
This is the main app that drives everything
"""
import dash
import dash_bootstrap_components as dbc
from dash import html
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.CYBORG],use_pages=True)
app.config['suppress_callback_exceptions'] = True

ASSETS_DIR = "/home/tjturnage/multipage/assets"
BASE_DIRECTORY = "/home/tjturnage/multipage"

top = html.Div([
    html.Br(),html.Br(),
])


header = dbc.Container(dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(class_name="flex-grow-1", children=
                [

                    dbc.Col(
                                       dbc.Nav(
                        [
                            dbc.NavLink(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app") and page["name"] in ["tw home"]
                        ]
                    ),
                    ),

                    dbc.Col(
                    dbc.DropdownMenu(
                        label="Forecast Stuff",
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app") and page["name"] in ["GRR AFDs"]
                        ],
                        nav=True,
                        in_navbar=True,
                    )
                    ),
                    dbc.Col(
                    dbc.DropdownMenu(
                        label="GR2Analyst",
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app") and page["name"] in ["Placefiles"]
                        ],
                        nav=True,
                        in_navbar=True,
                    )
                    ),
                    dbc.Col(
                    dbc.DropdownMenu(
                        label="Mesoanalysis",
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app") and page["name"] in ["SPC Meso Page", "SPC Mesoanalysis Loops"]
                        ],
                        nav=True,
                        in_navbar=True,
                    )
                    ),
                    dbc.Col(
                    dbc.DropdownMenu(
                        label="Projects",
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if not page["path"].startswith("/app") and page["name"] in ["GIMP", "Blender"]
                        ],
                        nav=True,
                        in_navbar=True,
                    )
                    ),
                ]
            )
        ],
        fluid=True,
    ),
    dark=True,
    color="dark"
))
app.layout = dbc.Container([top,header, dash.page_container], fluid=False)

if __name__ == '__main__':
    app.run_server(debug=True)
