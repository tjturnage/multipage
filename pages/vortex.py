# Import necessary libraries 
import dash
from dash import html #, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/vortex',
    title='Rankine Vortex',
    name='Rankine Vortex')

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
    <div class="container">
        <div class="row">
            <div class="col">
                <section>
                    <canvas id="c" width="600" height="600"></canvas>
                </section>
            </div>
            <div class="col">
                <div>
                    In the box below ... <br> Mouse right to increase translation<br>
                    Mouse up to increase convergence</div>
                <section>
                    <table id="sudoku" border="2">
                        <tbody>
                            <tr>
                                <td id="t0000" class="r"></td>
                                <td id="t0001" class="r"></td>
                                <td id="t0002" class="r"></td>
                                <td id="t0003" class="r"></td>
                                <td id="t0004" class="r"></td>
                                <td id="t0005" class="r"></td>
                                <td id="t0006" class="r"></td>
                                <td id="t0007" class="r"></td>
                                <td id="t0008" class="r"></td>
                                <td id="t0009" class="r"></td>
                                <td id="t0010" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0100" class="r"></td>
                                <td id="t0101" class="r"></td>
                                <td id="t0102" class="r"></td>
                                <td id="t0103" class="r"></td>
                                <td id="t0104" class="r"></td>
                                <td id="t0105" class="r"></td>
                                <td id="t0106" class="r"></td>
                                <td id="t0107" class="r"></td>
                                <td id="t0108" class="r"></td>
                                <td id="t0109" class="r"></td>
                                <td id="t0110" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0200" class="r"></td>
                                <td id="t0201" class="r"></td>
                                <td id="t0202" class="r"></td>
                                <td id="t0203" class="r"></td>
                                <td id="t0204" class="r"></td>
                                <td id="t0205" class="r"></td>
                                <td id="t0206" class="r"></td>
                                <td id="t0207" class="r"></td>
                                <td id="t0208" class="r"></td>
                                <td id="t0209" class="r"></td>
                                <td id="t0210" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0300" class="r"></td>
                                <td id="t0301" class="r"></td>
                                <td id="t0302" class="r"></td>
                                <td id="t0303" class="r"></td>
                                <td id="t0304" class="r"></td>
                                <td id="t0305" class="r"></td>
                                <td id="t0306" class="r"></td>
                                <td id="t0307" class="r"></td>
                                <td id="t0308" class="r"></td>
                                <td id="t0309" class="r"></td>
                                <td id="t0310" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0400" class="r"></td>
                                <td id="t0401" class="r"></td>
                                <td id="t0402" class="r"></td>
                                <td id="t0403" class="r"></td>
                                <td id="t0404" class="r"></td>
                                <td id="t0405" class="r"></td>
                                <td id="t0406" class="r"></td>
                                <td id="t0407" class="r"></td>
                                <td id="t0408" class="r"></td>
                                <td id="t0409" class="r"></td>
                                <td id="t0410" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0500" class="r"></td>
                                <td id="t0501" class="r"></td>
                                <td id="t0502" class="r"></td>
                                <td id="t0503" class="r"></td>
                                <td id="t0504" class="r"></td>
                                <td id="t0505" class="r"></td>
                                <td id="t0506" class="r"></td>
                                <td id="t0507" class="r"></td>
                                <td id="t0508" class="r"></td>
                                <td id="t0509" class="r"></td>
                                <td id="t0510" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0600" class="r"></td>
                                <td id="t0601" class="r"></td>
                                <td id="t0602" class="r"></td>
                                <td id="t0603" class="r"></td>
                                <td id="t0604" class="r"></td>
                                <td id="t0605" class="r"></td>
                                <td id="t0606" class="r"></td>
                                <td id="t0607" class="r"></td>
                                <td id="t0608" class="r"></td>
                                <td id="t0609" class="r"></td>
                                <td id="t0610" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0700" class="r"></td>
                                <td id="t0701" class="r"></td>
                                <td id="t0702" class="r"></td>
                                <td id="t0703" class="r"></td>
                                <td id="t0704" class="r"></td>
                                <td id="t0705" class="r"></td>
                                <td id="t0706" class="r"></td>
                                <td id="t0707" class="r"></td>
                                <td id="t0708" class="r"></td>
                                <td id="t0709" class="r"></td>
                                <td id="t0710" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0800" class="r"></td>
                                <td id="t0801" class="r"></td>
                                <td id="t0802" class="r"></td>
                                <td id="t0803" class="r"></td>
                                <td id="t0804" class="r"></td>
                                <td id="t0805" class="r"></td>
                                <td id="t0806" class="r"></td>
                                <td id="t0807" class="r"></td>
                                <td id="t0808" class="r"></td>
                                <td id="t0809" class="r"></td>
                                <td id="t0810" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t0900" class="r"></td>
                                <td id="t0901" class="r"></td>
                                <td id="t0902" class="r"></td>
                                <td id="t0903" class="r"></td>
                                <td id="t0904" class="r"></td>
                                <td id="t0905" class="r"></td>
                                <td id="t0906" class="r"></td>
                                <td id="t0907" class="r"></td>
                                <td id="t0908" class="r"></td>
                                <td id="t0909" class="r"></td>
                                <td id="t0910" class="r"></td>
                            </tr>
                            <tr>
                                <td id="t1000" class="r"></td>
                                <td id="t1001" class="r"></td>
                                <td id="t1002" class="r"></td>
                                <td id="t1003" class="r"></td>
                                <td id="t1004" class="r"></td>
                                <td id="t1005" class="r"></td>
                                <td id="t1006" class="r"></td>
                                <td id="t1007" class="r"></td>
                                <td id="t1008" class="r"></td>
                                <td id="t1009" class="r"></td>
                                <td id="t1010" class="r"></td>
                            </tr>
                        </tbody>
                    </table>
                </section>
                <section>
                    <div>Max Rotation: 10</div>
                    <div id="trans"></div>
                    <div id="conv"></div>
                </section>
            </div>



        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
    <script>
        function create_graph(conv, trans) {
            ctx = document.getElementById("c").getContext("2d");
            ctx.lineWidth = 4;
            ctx.clearRect(0, 0, 600, 600);
            ctx.strokeStyle = 'rgba(0,0,0,0.15)';
            ctx.beginPath();
            ctx.arc(300, 300, 200, 0, 2 * Math.PI);
            //ctx.moveTo(200, 0);
            //ctx.lineTo(400, 0);
            //ctx.moveTo(0,200);
            //ctx.lineTo(0,400);
            //ctx.strokeStyle = 'rgb(125,125,125)';
            ctx.stroke();
            for (var i = 0; i < 900; i += 25) {
                for (var j = 0; j < 900; j += 25) {

                    rotation(ctx, i, j, conv, trans);
                }
            }

        }


        function rotation(ctx, x, y, conv, trans) {

            const r_max = 200;
            var headlen = 5;
            var dx = 300 - x;
            var dy = 300 - y;
            var angle = Math.atan2(dy, dx);
            var sina = Math.sin(angle)
            var cosa = Math.cos(angle)
            var distance = Math.sqrt(dx ** 2 + dy ** 2);
            let inner_r_coef = distance / r_max;
            let outer_r_coef = (r_max / distance) ** 2;
            var unit = 10;


            if (distance < r_max) {
                var coef = inner_r_coef;
            } else {
                var coef = outer_r_coef;
            }

            var fmx = x + unit * coef * sina;
            var tox = x - unit * coef * sina + trans;
            var fmy = y - unit * coef * cosa;
            var toy = y + unit * coef * cosa;

            // create proportional vector length option    
            fmx = fmx - conv * coef * cosa;
            tox = tox + conv * coef * cosa;
            fmy = fmy - conv * coef * sina;
            toy = toy + conv * coef * sina;

            // new_angle is orientation of vector instead of position from origin
            var full_mag = Math.sqrt((toy - fmy) ** 2 + (tox - fmx) ** 2);
            var new_angle = Math.atan2(toy - fmy, tox - fmx)

            // create uniform vector length option
            // this requires both magnitude and direction from the full magnitude vector
            //
            fmx = x - (unit * Math.cos(new_angle));
            tox = x + (unit * Math.cos(new_angle));
            fmy = y - (unit * Math.sin(new_angle));
            toy = y + (unit * Math.sin(new_angle));


            ctx.lineWidth = 1
            if (full_mag > 33) {
                ctx.lineWidth = 3
                var stroke_color = 'rgb(128,0,128';
            } else if (full_mag > 27) {
                ctx.lineWidth = 2.5
                var stroke_color = 'rgb(225, 87, 51)';
            } else if (full_mag > 24) {
                ctx.lineWidth = 2
                var stroke_color = 'rgba(200, 170, 0.9)';
            } else if (full_mag > 22) {
                ctx.lineWidth = 1.5
                var stroke_color = 'rgba(200, 170, 0.8)';
            } else if (full_mag > 20) {
                var stroke_color = 'rgba(0, 125, 0,0.8)';
            } else if (full_mag > 14) {
                var stroke_color = 'rgba(0, 125, 0,0.6)';
            } else if (full_mag > 12) {
                var stroke_color = 'rgba(0, 0,0,0.6)';
            } else if (full_mag > 8) {
                var stroke_color = 'rgba(0, 0,0,0.5)';
            } else if (full_mag > 4) {
                var stroke_color = 'rgba(0, 0,0,0.4)';
            } else {
                var stroke_color = 'rgba(0, 0,0,0.2)';
            }



            ctx.beginPath();
            ctx.moveTo(fmx, fmy);
            ctx.lineTo(tox, toy);
            ctx.moveTo(tox, toy);
            ctx.lineTo(tox - headlen * Math.cos(new_angle - Math.PI / 6), toy - headlen * Math.sin(new_angle - Math
                .PI / 6));
            ctx.moveTo(tox, toy);
            ctx.lineTo(tox - headlen * Math.cos(new_angle + Math.PI / 6), toy - headlen * Math.sin(new_angle + Math
                .PI / 6));
            ctx.strokeStyle = stroke_color;
            ctx.stroke();
            //function plot_arrow()
            //return;
        }


        function get_values(id) {

            var conv = 10 - parseFloat(id.slice(1, 3));
            var trans = parseFloat(id.slice(3, 5));
            var convergence = 'Max Convergence: ' + conv.toString();
            var translation = 'Max Translation: ' + trans.toString();
            document.getElementById('conv').innerText = convergence;
            document.getElementById('trans').innerText = translation;

            create_graph(conv, trans);

        };

        const squares = document.querySelectorAll(".r");

        squares.forEach(square => {
            square.addEventListener('mouseenter', e => {

                document.getElementById(e.target.id).classList.add('highlight');
                let el = document.getElementById(e.target.id);
                //console.log(e.target.id)
                get_values(e.target.id);
            })
        });

        squares.forEach(square => {
            square.addEventListener('mouseleave', e => {
                document.getElementById(e.target.id).classList.remove('highlight');
            })
        });
    </script>
</body>

</html>
"""

# Define the page layout
def layout():
    """mesoanalysis page layout

    Returns:
        None
    """
    return dbc.Container([
      dbc.Row([
          dbc.Col(
              html.Iframe(
                  srcDoc=EMBEDDED_HTML,
                  style={'width': '100%', 'height': '650px'}
              )
          )
        ],style={'padding':'0.5em'}),
            ])
