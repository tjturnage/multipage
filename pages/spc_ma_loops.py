# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/spc_ma_loops',
    title='SPC Mesoanalysis Loops',
    name='SPC Mesoanalysis Loops',
    order=4)


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
    <title>SPC Meso loops</title>
    <style>
        body {
            background-color: rgb(240, 240, 240);
        }

        .display-image {
            width: 900px;
            height: 600px;
            background-repeat: no-repeat;
            background-position: 50% 50%;
            background-size: cover;
            object-fit: contain;
            background-color: rgb(250, 250, 250);
        }

        .image {
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0.05rem;
            border-radius: 5px;
            min-height: 1.8rem;
        }

        .description-highlight {
            color: red;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .slider {
            padding: 0.3em;
            align-self: center;
            align-content: center;
            align-items: center;
        }

        .strong {
            font-weight: bolder;
            font-size: 1.3em
        }
    </style>
</head>

<body>
    <br>
    <div class="container stretch">

        <div class="container">
            <div class="justify-content-center text-center">
                <span><b>Sector:&nbsp;&nbsp;&nbsp;&nbsp;</b></span>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s19" value="s19">
                    <label class="form-check-label" for="greatlakes">CONUS</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s21" value="s21" checked>
                    <label class="form-check-label" for="greatlakes">Wrn GL</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s16" value="s16">
                    <label class="form-check-label" for="greatlakes">NE & GL</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s17" value="s17">
                    <label class="form-check-label" for="greatlakes">Mid Atl</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s18" value="s18">
                    <label class="form-check-label" for="greatlakes">SE</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s13" value="s13">
                    <label class="form-check-label" for="greatlakes">N Plains</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s20" value="s20">
                    <label class="form-check-label" for="greatlakes">Midwest</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s14" value="s14">
                    <label class="form-check-label" for="greatlakes">C Plains</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s15" value="s15">
                    <label class="form-check-label" for="greatlakes">S Plains</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s11" value="s11">
                    <label class="form-check-label" for="greatlakes">NW</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input radio" type="radio" name="mesoSector" id="s12" value="s12">
                    <label class="form-check-label" for="greatlakes">SW</label>
                </div>
            </div>
            <div class="container">
                <div class="justify-content-center text-center">
                    <button type="button" class="btn btn-outline-primary btn-sm" id="pmsl">Press/Wind</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="ttd">Temp/Wind/Dwpt</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="thea">Theta-E Adv</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="925mb">925mb</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="850mb2">850mb</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="850mb">850mb v2</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="700mb">700mb</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="500mb">500mb</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="300mb">300mb</button>
                    <button type="button" class="btn btn-outline-primary btn-sm" id="dlcp">Deep Moist Conv</button>
                    <button type="button" class="btn btn-outline-info btn-sm" id="mlcp">MLCAPE</button>
                    <button type="button" class="btn btn-outline-info btn-sm" id="dcape">DCAPE</button>
                    <button type="button" class="btn btn-outline-info btn-sm" id="laps">Mid Lapse Rate</button>
                    <button type="button" class="btn btn-outline-info btn-sm" id="lllr">Low Lapse Rate</button>
                    <button type="button" class="btn btn-outline-dark btn-sm" id="eshr">Eff Bulk Shear </button>
                    <button type="button" class="btn btn-outline-dark btn-sm" id="effh">Eff SRH</button>
                    <button type="button" class="btn btn-outline-dark btn-sm" id="brns">BRN Shear</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="scp">Supercell Comp</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="stpc">Sig Tor (eff)</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="cbsig">C/B SigSvr</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="lr3c">0-3 LR/MLCAPE</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="3cvr">Sfc Vort & 0-3 MLCAPE</button>
                    <button type="button" class="btn btn-outline-danger btn-sm" id="moshe">Mod SHERBE</button>

                </div>
            </div>

            <div class="container-fluid slider">
                <div class="row justify-content-center text-center">
                    <div class="col-sm-12"><label for="this_url" class="form-label strong">Move Slider To Adjust
                            Time</label></div>
                </div>
                <div class="row justify-content-center text-center">
                    <div class="col-sm-12"><input class="this_url" type="range" class="form-range" id="this_url"
                            name="times" min="0" max="10"></div>
                </div>
            </div>

            <div class="container-fluid">
                <div class="d-flex justify-content-center text-center">
                    <div class="row fit">
                        <img id="display-image" class="img-fluid display-image"
                            src="https://www.spc.noaa.gov/exper/mesoanalysis/s21/mlcp/mlcp.gif">
                    </div>
                </div>
            </div>

</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
</script>
<script>
    const minutesToAdjust = 60;
    const millisecondsPerMinute = 60000;
    const hours = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6];
    var prod = 'mlcp'
    let sector = 's21/'
    const baseURL = 'https://www.spc.noaa.gov/exper/mesoanalysis/'
    const fcstURL = baseURL + 'fcst/'
    const input = document.querySelector('.this_url');
    var urls = create_urls();
    const radios = document.querySelectorAll(".radio");
    const buttons = document.querySelectorAll("button");
    const images = document.querySelectorAll("div.image");

    input.addEventListener('input', getImage);

    function changeSector(e) {
        reference_id = e.target.id
        sector = reference_id.slice(0, 3) + '/';
        urls = create_urls();
    }

    function changeProduct(e) {
        reference_id = e.target.id
        prod = reference_id;
        urls = create_urls();
    }

    for (const radio of radios) {
        radio.addEventListener('change', changeSector);
    };

    buttons.forEach(btn => {
        btn.addEventListener('click', b => {
            changeProduct(b);
        })
    });

    images.forEach(image => {
        image.addEventListener('click', c => {
            changeProduct(c);
        })
    });

    function getDescription(d) {
        for (var i = 0; i < images.length; i++) {
            images[i].classList.remove('description-highlight');
        }

        let reference_id = d.target.id;
        console.log(reference_id)
        let desc = descriptions[reference_id];
        document.getElementById(reference_id).classList.add('description-highlight');
        if (desc === undefined) {
            document.getElementById('describe').innerHTML = 'Product Description Not Available';
        } else {
            document.getElementById('describe').innerHTML = desc;
        }
    }


    function refreshImage(imgURL) {
        let date = new Date();
        let date_string = make_datestring(date, true);
        var queryString = "?t=" + date_string;
        newSrc = imgURL + queryString;
        return newSrc
    }

    function getImage(e) {
        url = urls[e.target.value]
        document.getElementById('display-image').src = url;
    }


    function padTo2Digits(num) {
        return num.toString().padStart(2, '0');
    }

    // https://www.spc.noaa.gov/exper/mesoanalysis/s16/mlcp/mlcp_22061720.gif
    // https://www.spc.noaa.gov/exper/mesoanalysis/fcst/s16/mlcp_01.gif
    function image_URL(ds, h, minutes) {
        let futureURL = fcstURL + sector + prod + '_' + ds.slice(-2) + '.gif';
        let pastURL = baseURL + sector + prod + '/' + prod + '_' + ds + '.gif';
        let currentURL = baseURL + sector + prod + '/' + prod + '.gif';
        if (h > 0) {
            return futureURL;
        }
        if (h < 0) {
            ;
            return pastURL;
        }
        if (h === 0) {
            return currentURL;
        }
        return;
    }

    function make_datestring(date, include_minutes) {
        // include_minutes is a boolean variable
        let minutes = date.getMinutes();
        var min_str = '00';
        if (minutes > 20) {
            min_str = '20';
        }
        if (minutes > 40) {
            min_str = '40';
        }
        let date_string = [
            date.getUTCFullYear().toString().slice(-2),
            padTo2Digits(date.getUTCMonth() + 1),
            padTo2Digits(date.getUTCDate()),
            padTo2Digits(date.getUTCHours()),
            min_str
        ].join('');
        console.log(date_string);
        if (include_minutes) {
            return date_string;
        }
        return date_string.slice(0, -2);
    }

    function create_urls() {
        let urls = []
        let now = new Date();
        let minutes = now.getMinutes()
        hours.forEach(h => {
            let date = new Date(now.valueOf() + (h * minutesToAdjust * millisecondsPerMinute));
            let date_string = make_datestring(date, false);
            let url = image_URL(date_string, h, minutes);
            let new_url = refreshImage(url);
            urls.push(new_url);
        })
        return urls;
    };
</script>

</html>

"""

mesoanalysis = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Iframe(
                srcDoc=EMBEDDED_HTML,
                style={'width': '100%', 'height': '900px'}
            )
        )
    ], style={'padding': '0.5em'}),
])


title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("SPC Mesoanalysis Loops"), width=12)])
    ])

# Define the page layout
def layout():
    """mesoanalysis page layout

    Returns:
        None
    """
    return dbc.Container([title, mesoanalysis])
