# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/placefiles',
    title='Placefiles',
    name='Placefiles',
    order=2)

EMBEDDED_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>
        td {
            border: 0.1em solid #0000;
            border-radius: 5px;
            width: 30px;
            height: 30px;
            text-align: center;
            transition: 0.3s;
        }

        .highlight {
            /* font-weight: bold; */
            /*min-height: 2rem; */
            background-color: rgb(185, 185, 234);
            /*font-weight: bold;*/
        }
    </style>


    <title>Simulated Tornado Vortex</title>
</head>
<body>
<h1>Placefiles</h1>
<h4>Data displays are time matched to radar data, now includes <a href="https://mesowest.utah.edu/cgi-bin/droman/mesomap.cgi?product=roads&state=MI&address=&urlParamsOverride=1&zoom=&radius=25" target="_blank">Michigan RWIS data!</a></h4>
<ul>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/latest_surface_observations.txt">Surface obs - All elements</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/latest_surface_observations_lg.txt">Surface obs - All elements - large font</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/latest_surface_observations_xlg.txt">Surface obs - All elements - extra large font</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/temp.txt">Air Temperature</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/dwpt.txt">Dewpoint Temperature</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/road.txt">MI Road Temperature</a></li>
  <li><a href="https://tjturnage.pythonanywhere.com/assets/wind.txt">Wind and Gust</a></li>
</ul>
<br>
</body>
</html>
"""

bullet_list = dbc.Col(
    html.Ul([
        html.Li(html.A("Surface Obs", \
        href="assets/latest_surface_observations.txt")),
        html.Li(html.A("Surface Obs - large font", \
        href="assets/latest_surface_observations_lg.txt")),
        html.Li(html.A("Surface Obs - extra large font", \
        href="assets/latest_surface_observations_xlg.txt")),
        html.Li(html.A("Air Temperature", \
        href="assets/temp.txt")),
        html.Li(html.A("Dewpoint Temperature", \
        href="assets/dwpt.txt")),
        html.Li(html.A("MI Road Temperature", \
        href="assets/road.txt")),
        html.Li(html.A("Wind and Gust", \
        href="assets/wind.txt")),
    ])
)

# Define the page layout
def layout():
    """mesoanalysis page layout

    Returns:
        None
    """
    return dbc.Container(bullet_list)

# def layout():
#     """mesoanalysis page layout

#     Returns:
#         None
#     """
#     return dbc.Container([
#       dbc.Row([
#           dbc.Col(
#               html.Iframe(
#                   srcDoc=EMBEDDED_HTML,
#                   style={'width': '100%', 'height': '980px'}
#               )
#           )
#         ],style={'padding':'0.5em'}),
#             ])