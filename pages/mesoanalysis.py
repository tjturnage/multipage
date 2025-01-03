# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
    path='/mesoanalysis',
    title='mesoanalysis',
    name='SPC Meso Page',
    order=3)

EMBEDDED_HTML = """
<!DOCTYPE html>
<html lang="en">

<!--
-----------------------------------------------------------------------------
12/12/2022 - Version 1.04
Added SPC sector 21 (Western Great Lakes)
Added SPC sector 20 (Midwest)

please email thomas.turnage@noaa.gov for bug reports or suggestions
-----------------------------------------------------------------------------
-->

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>
        body {
            background-color: rgb(240, 240, 240);
        }

        h4 {
            padding: 0.2rem;
            background-color: rgb(236, 236, 236);
            border: 1px solid black;
            text-align: center;
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

        .time {
            min-height: 1.8rem;
            font-weight: bold;
            background-color: rgb(240, 240, 240);
        }

        .instructions {
            font-weight: bold;
            border-radius: 5px;
            background-color: rgb(245, 245, 245);
        }


        .instructions-hover {
            border-radius: 5px;
            background-color: rgb(185, 185, 234);

        }

        .instructions-click {
            color:rgb(250, 0, 0)
        }


        .description-highlight {
            color: red;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .highlight {
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0.05rem;
            border-radius: 5px;
            min-height: 1.8rem;
            background-color: rgb(185, 185, 234);
        }

        .spc-prod {
            font-size: 0.9rem;
            font-family: arial;
            color: #990000;
            font-weight: bold;
        }

        .sat-prod {
            font-size: 1.0rem;
            font-family: arial;
            color: #990000;
            font-weight: bold;
        }


        .spc-info {
            font-size: 0.7rem;
            font-family: arial;
        }

        .sat-info {
            font-size: 1.0rem;
            font-family: arial;
            font-weight: bold;
        }

        .description box {
            min-width: 900px;
        }

        .spc-ref {
            font-size: 0.6rem;
            font-family: arial;
        }

        a:hover {
            color: rgb(255, 255, 83);
            background-color: rgb(185, 185, 234);
            padding: 0.2rem;
        }

        .stretch {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }

        .display-image {
            width: 900px;
            height: 600px;
            background-repeat: no-repeat;
            background-position: 50% 50%;
            background-size: cover;
            object-fit: contain;
            background-color: rgb(245, 245, 245);
        }

        .us-loop {

            color: rgb(172, 0, 0);
            /*border-style: solid;
            border-width: 1px;*/

        }

        .sector-loop {
            color: rgb(0, 9, 139);
            /*border-style: solid;
            border-width: 1px;*/
        }

        .rd {
            background-image: url("http://www.spc.noaa.gov/exper/mesoanalysis/s14/rgnlrad/rgnlrad.gif?1278279059554");
            width: 901px;
            height: 601px;
            background-repeat: no-repeat;
            background-position: 50% 50%;
            background-size: cover;
            object-fit: contain;

        }

        a:link {
            text-decoration: none;
        }
    </style>
    <title>Mesoanalysis</title><br>
</head>

<body>
    <div class="container stretch">
        <div class="justify-content-center text-center">
            <span><b>Sector:&nbsp;&nbsp;&nbsp;&nbsp;</b></span>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s21gl" value="s21" checked>
                <label class="form-check-label" for="greatlakes">Wrn GL</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s16gl" value="s16">
                <label class="form-check-label" for="greatlakes">GL</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s16ne" value="s16">
                <label class="form-check-label" for="greatlakes">NE</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s17" value="s17">
                <label class="form-check-label" for="greatlakes">Mid Atl</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s18se" value="s18">
                <label class="form-check-label" for="greatlakes">SE</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s18smv" value="s18">
                <label class="form-check-label" for="greatlakes">S Miss Val</label>
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
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s11nw" value="s11">
                <label class="form-check-label" for="greatlakes">NW</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s11nr" value="s11">
                <label class="form-check-label" for="greatlakes">N Rock</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s12sw" value="s12">
                <label class="form-check-label" for="greatlakes">SW</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input radio" type="radio" name="mesoSector" id="s12sr" value="s12">
                <label class="form-check-label" for="greatlakes">S Rock</label>
            </div>


        </div>
        <div class="justify-content-center text-center">
            <button type="button" class="btn btn-outline-danger btn-sm" id="swody1">DY1</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="swody2">DY2</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="spc_watch">Watches</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="surface">Sfc</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="upper">Upper</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="ma-stability">Thermo</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="ma-shear">Shear</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="ma-composite">Comp</button>
            <button type="button" class="btn btn-outline-danger btn-sm" id="ma-multiparm">Multi</button>
            <!-- <button type="button" class="btn btn-primary" id="swody3">swody3</button> -->
            <button type="button" class="btn btn-outline-success btn-sm" id="wpc">Precip</button>
            <button type="button" class="btn btn-outline-success btn-sm" id="ma-fire">Fire</button>
            <button type="button" class="btn btn-outline-success btn-sm" id="ma-winter">Winter</button>
            <button type="button" class="btn btn-outline-info btn-sm" id="sounding">RAOB</button>
            <button type="button" class="btn btn-outline-info btn-sm" id="radar">Radar</button>
            <button type="button" class="btn btn-outline-info btn-sm" id="satellite">Sat</button>
            <button type="button" class="btn btn-outline-secondary btn-sm" id="links">Links</button>
        </div>

        <div class="container-fluid">
            <div class="d-flex justify-content-center text-center">
                <div class="row">
                    <div class="instructions" id="instructions">
                        <span class="instructions-hover">Hover over products for maps</span>  
                        <span class="instructions-click">Click a product for description under map</span>
                </div>
            </div>
        </div>

    </div>
    <div class="container-fluid">
        <div class="d-flex justify-content-center text-center">

            <div class="divider" id="section_swody1">
                <div class="row">
                    <div class="row">
                        <div class="col-sm-2 time"><a href="https://www.spc.noaa.gov/products/outlook/day1otlk.html"
                                target="_blank">Most Recent</a></div>
                        <div class="col-sm-2 image" id="dy1_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy1_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy1_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy1_torn">Tornado</div>
                    </div>

                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day1otlk_0100.html" target="_blank">0100
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy1_0100_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy1_0100_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy1_0100_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy1_0100_torn">Tornado</div>
                    </div>

                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day1otlk_0600.html" target="_blank">0600
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy1_0600_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy1_0600_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy1_0600_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy1_0600_torn">Tornado</div>
                    </div>

                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day1otlk_1300.html" target="_blank">1300
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy1_1300_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy1_1300_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy1_1300_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy1_1300_torn">Tornado</div>
                    </div>

                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day1otlk_1630.html" target="_blank">1630
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy1_1630_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy1_1630_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy1_1630_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy1_1630_torn">Tornado</div>
                    </div>
                </div>
            </div>

            <div class="divider" id="section_swody2">
                <div class="row">
                    <div class="row">
                        <div class="col-sm-2 time"><a href="https://www.spc.noaa.gov/products/outlook/day2otlk.html"
                                target="_blank">Most Recent</a></div>
                        <div class="col-sm-2 image" id="dy2_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy2_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy2_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy2_torn">Tornado</div>
                    </div>
                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day2otlk_0600.html" target="_blank">0600
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy2_0600_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy2_0600_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy2_0600_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy2_0600_torn">Tornado</div>

                    </div>
                    <div class="row">
                        <div class="col-sm-2 time"><a
                                href="https://www.spc.noaa.gov/products/outlook/day2otlk_1730.html" target="_blank">1730
                                UTC</a></div>
                        <div class="col-sm-2 image" id="dy2_1730_otlk">Outlook</div>
                        <div class="col-sm-2 image" id="dy2_1730_hail">Hail</div>
                        <div class="col-sm-2 image" id="dy2_1730_wind">Wind</div>
                        <div class="col-sm-2 image" id="dy2_1730_torn">Tornado</div>
                    </div>
                </div>
            </div>

            <div class="divider" id="section_spc_watch">
                <div class="row">
                    <div class="col-sm-2 time"><a href="https://www.spc.noaa.gov/products/md/" target="_blank">Meso
                            Page</a></div>
                    <div class="col-sm-2 time"><a href="https://www.spc.noaa.gov/products/watch/"
                            target="_blank">Watches Page</a></div>
                    <div class="col-sm-2 time"><a href="https://www.spc.noaa.gov/climo/online/#reports"
                            target="_blank">Reports Page</a></div>
                    <div class="col-sm-2 image" id="s-mds">Meso Disc</div>
                    <div class="col-sm-2 image" id="s-watch">Watches</div>
                    <div class="col-sm-2 image" id="rpts">Storm Rpts</div>
                </div>
            </div>

            <div class="divider" id="section_surface">
                <div class="row">

                    <div class="col-sm-2 image nr" id="pmsl">Pressure and Wind</div>
                    <div class="col-sm-2 image nr" id="bigsfc">Surface Plot</div>
                    <div class="col-sm-2 image nr" id="ttd">Temp/Wind/Dwpt</div>
                    <div class="col-sm-2 image nr" id="thet">MSL Press/Theta-e/Wind</div>
                    <div class="col-sm-2 image nr" id="mcon">Moisture Convergence</div>
                    <div class="col-sm-2 image nr" id="thea">Theta-E Advection</div>
                    <div class="col-sm-2 image nr" id="mxth">Mixing Ratio / Theta</div>
                    <div class="col-sm-2 image nr" id="icon">Inst Contraction Rate</div>
                    <div class="col-sm-2 image nr" id="trap">Fluid Trapping</div>
                    <div class="col-sm-2 image nr" id="vtm">Velocity Tensor Mag</div>
                    <div class="col-sm-2 image nr" id="dvvr">Sfc Div and Vort</div>
                    <div class="col-sm-2 image nr" id="def">Deformation / Axis of Dilitation</div>
                    <div class="col-sm-2 image nr" id="pchg">2hr Press Change</div>
                    <div class="col-sm-2 image nr" id="temp_chg">3hr Temp Change</div>
                    <div class="col-sm-2 image nr" id="dwpt_chg">3hr Dewpoint Change</div>
                    <div class="col-sm-2 image nr" id="mixr_chg">3hr 100mb MixR Change</div>
                    <div class="col-sm-2 image nr" id="thte_chg">3hr Thetae Change</div>
                </div>
            </div>

            <div class="divider" id="section_upper">
                <div class="row">
                    <div class="col-sm-2 image nr" id="925mb">925mb Analysis</div>
                    <div class="col-sm-2 image nr" id="850mb2">850mb Analysis</div>
                    <div class="col-sm-2 image nr" id="850mb">850mb Analysis v2</div>
                    <div class="col-sm-2 image nr" id="700mb">700mb Analysis</div>
                    <div class="col-sm-2 image nr" id="500mb">500mb Analysis</div>
                    <div class="col-sm-2 image nr" id="300mb">300mb Analysis</div>
                    <div class="col-sm-2 image nr" id="dlcp">Deep Moist Conv</div>
                    <div class="col-sm-2 image nr" id="tadv_925">925mb Temp Adv</div>
                    <div class="col-sm-2 image nr" id="tadv">850mb Temp Adv</div>
                    <div class="col-sm-2 image nr" id="7tad">700mb Temp Adv</div>
                    <div class="col-sm-2 image nr" id="sfnt">Surface FGEN</div>
                    <div class="col-sm-2 image nr" id="9fnt">925mb FGEN</div>
                    <div class="col-sm-2 image nr" id="8fnt">850mb FGEN</div>
                    <div class="col-sm-2 image nr" id="7fnt">700mb FGEN</div>
                    <div class="col-sm-2 image nr" id="epvl">850 fgen & EPV</div>
                    <div class="col-sm-2 image nr" id="epvm">700 fgen & EPV</div>
                    <div class="col-sm-2 image nr" id="98ft">925-850mb FGEN</div>
                    <div class="col-sm-2 image nr" id="857f">850-700mb FGEN</div>
                    <div class="col-sm-2 image nr" id="75ft">700-500mb FGEN</div>
                    <div class="col-sm-2 image nr" id="vadv">700-400mb Diff PVA</div>
                    <div class="col-sm-2 image nr" id="padv">400-250mb Pot Vort Adv</div>
                    <div class="col-sm-2 image nr" id="ddiv">850-250mb Diff Div</div>
                    <div class="col-sm-2 image nr" id="ageo">300mb Jet Circ</div>
                    <div class="col-sm-2 image nr" id="500mb_chg">12hr H5 chg</div>
                    <div class="col-sm-2 image nr" id="trap_500">Fluid Trapping (H500)</div>
                    <div class="col-sm-2 image nr" id="trap_250">Fluid Trapping (H250)</div>
                </div>
            </div>

            <div class="divider" id="section_ma-stability">
                <div class="row">
                    <div class="col-sm-2 image nr" id="sbcp">SBCAPE</div>
                    <div class="col-sm-2 image nr" id="mlcp">MLCAPE</div>
                    <div class="col-sm-2 image nr" id="mucp">MUCAPE</div>
                    <div class="col-sm-2 image nr" id="eltm">EL Temp/MUCAPE/MUCIN</div>
                    <div class="col-sm-2 image nr" id="ncap">CAPE - Normalized</div>
                    <div class="col-sm-2 image nr" id="dcape">CAPE - Downdraft</div>
                    <div class="col-sm-2 image nr" id="muli">Sfc Based LI</div>
                    <div class="col-sm-2 image nr" id="laps">Mid-Level Lapse Rates</div>
                    <div class="col-sm-2 image nr" id="lllr">Low-Level Lapse Rates</div>
                    <div class="col-sm-2 image nr" id="maxlr">Max 2-6 km AGL Lapse Rate</div>
                    <div class="col-sm-2 image nr" id="lclh">LCL hght</div>
                    <div class="col-sm-2 image nr" id="lfch">LFC hght</div>
                    <div class="col-sm-2 image nr" id="lfrh">LCL-LFC RH</div>
                    <div class="col-sm-2 image nr" id="sbcp_chg">3-hour SBCAPE Change</div>
                    <div class="col-sm-2 image nr" id="sbcn_chg">3-hour SBCIN Change</div>
                    <div class="col-sm-2 image nr" id="mlcp_chg">3-hour MLCAPE Change</div>
                    <div class="col-sm-2 image nr" id="mucp_chg">3-hour MUCAPE Change</div>
                    <div class="col-sm-2 image nr" id="lllr_chg">3-hour Low LR Change</div>
                    <div class="col-sm-2 image nr" id="laps_chg">6-hour Mid LR Change</div>
                    <div class="col-sm-2 image nr" id="skewt">Skew-T Maps</div>
                    <div class="col-sm-2 image nr" id="ttot">Total Totals</div>
                    <div class="col-sm-2 image nr" id="show">Showalter Index</div>
                    <div class="col-sm-2 image nr" id="kidx">K Index</div>

                </div>
            </div>

            <div class="divider" id="section_ma-shear">
                <div class="row">
                    <div class="col-sm-2 image nr" id="eshr">Bulk Shear - Effective</div>
                    <div class="col-sm-2 image nr" id="shr6">Bulk Shear - Sfc-6km</div>
                    <div class="col-sm-2 image nr" id="shr8">Bulk Shear - Sfc-8km</div>
                    <div class="col-sm-2 image nr" id="shr3">Bulk Shear - Sfc-3km</div>
                    <div class="col-sm-2 image nr" id="shr1">Bulk Shear - Sfc-1km</div>
                    <div class="col-sm-2 image nr" id="brns">BRN Shear</div>
                    <div class="col-sm-2 image nr" id="effh">SR Helicity - Effective</div>
                    <div class="col-sm-2 image nr" id="srh3">SR Helicity - Sfc-3km</div>
                    <div class="col-sm-2 image nr" id="srh1">SR Helicity - Sfc-1km</div>
                    <div class="col-sm-2 image nr" id="srh5">SR Helicity - Sfc-500m</div>
                    <div class="col-sm-2 image nr" id="llsr">SR Wind - Sfc-2km</div>
                    <div class="col-sm-2 image nr" id="mlsr">SR Wind - 4-6km</div>
                    <div class="col-sm-2 image nr" id="ulsr">SR Wind - 9-11km</div>
                    <div class="col-sm-2 image nr" id="alsr">SR Wind - Anvil Level</div>
                    <div class="col-sm-2 image nr" id="mnwd">850-300mb Mean Wind</div>
                    <div class="col-sm-2 image nr" id="xover">850 and 500mb Winds</div>
                    <div class="col-sm-2 image nr" id="srh3_chg">3hr Sfc-3km SR Helicity Change</div>
                    <div class="col-sm-2 image nr" id="shr1_chg">3hr Sfc-1km Bulk Shear Change</div>
                    <div class="col-sm-2 image nr" id="shr6_chg">3hr Sfc-6km Bulk Shear Change</div>
                    <div class="col-sm-2 image nr" id="hodo">Hodograph Map</div>
                </div>
            </div>

            <div class="divider" id="section_ma-composite">
                <div class="row">
                    <div class="col-sm-2 image nr" id="scp">Supercell Composite</div>
                    <div class="col-sm-2 image nr" id="stor">Sig Tor (fixed)</div>
                    <div class="col-sm-2 image nr" id="stpc">Sig Tor (eff)</div>
                    <div class="col-sm-2 image nr" id="stpc5">Sig Tor (0-500m SRH)</div>
                    <div class="col-sm-2 image nr" id="sigt1">Cond Prob SigTor 1</div>
                    <div class="col-sm-2 image nr" id="sigt2">Cond Prob SigTor 2</div>
                    <div class="col-sm-2 image nr" id="nstp">Non-Supercell Tor</div>
                    <div class="col-sm-2 image nr" id="vtp3">Violent Tor Parm</div>
                    <div class="col-sm-2 image nr" id="sigh">Significant Hail</div>
                    <div class="col-sm-2 image nr" id="sars1">SARS Hail Size</div>
                    <div class="col-sm-2 image nr" id="sars2">SARS Hail %age</div>
                    <div class="col-sm-2 image nr" id="lghl">Large Hail Parm</div>
                    <div class="col-sm-2 image nr" id="dcp">Derecho Comp</div>
                    <div class="col-sm-2 image nr" id="cbsig">Craven/Brooks SigSvr</div>
                    <div class="col-sm-2 image nr" id="brn">Bulk Ri Number</div>
                    <div class="col-sm-2 image nr" id="mcsm">MCS Maint</div>
                    <div class="col-sm-2 image nr" id="mbcp">Microburst Composite</div>
                    <div class="col-sm-2 image nr" id="desp">Enh Stretch Pot</div>
                    <div class="col-sm-2 image nr" id="ehi1">EHI - Sfc-1km</div>
                    <div class="col-sm-2 image nr" id="ehi3">EHI - Sfc-3km</div>
                    <div class="col-sm-2 image nr" id="vgp3">VGP - Sfc-3km</div>
                    <div class="col-sm-2 image nr" id="crit">Critical Angle</div>
                    <div class="col-sm-2 image nr" id="sherbe">SHERBE</div>
                    <div class="col-sm-2 image nr" id="moshe">Modified SHERBE</div>
                    <div class="col-sm-2 image nr" id="cwasp">CWASP</div>
                    <div class="col-sm-2 image nr" id="tehi">Tornadic 0-1 km EHI</div>
                    <div class="col-sm-2 image nr" id="tts">Tornadic Tilting and Stretching parameter (TTS)</div>
                    <div class="col-sm-2 image nr" id="ptstpe">Conditional probability of EF0+ tornadoes</div>
                    <div class="col-sm-2 image nr" id="pstpe">Conditional probability of EF2+ tornadoes</div>
                    <div class="col-sm-2 image nr" id="pvstpe">Conditional probability of EF4+ tornadoes</div>
                </div>
            </div>


            <div class="divider" id="section_ma-multiparm">
                <div class="row">
                    <div class="col-sm-2 image nr" id="mlcp_eshr">MLCAPE / Eff Shear</div>
                    <div class="col-sm-2 image nr" id="cpsh">MUCAPE / Eff Shear</div>
                    <div class="col-sm-2 image nr" id="comp">MU LI / H8 & H5 Wind</div>
                    <div class="col-sm-2 image nr" id="lcls">LCL Hgt / 0-1 SRH</div>
                    <div class="col-sm-2 image nr" id="lr3c">0-3km Lapse Rate/MLCAPE</div>
                    <div class="col-sm-2 image nr" id="3cape_shr3">0-3km Bulk Shear/MLCAPE</div>
                    <div class="col-sm-2 image nr" id="3cvr">Sfc Vort / 0-3km MLCAPE</div>
                    <div class="col-sm-2 image nr" id="tdlr">Sfc Dwpt / H7-H5 LapseR</div>
                    <div class="col-sm-2 image nr" id="qlcs1">0-3km ThetaE diff/Shear Vec & MUCAPE</div>
                    <div class="col-sm-2 image nr" id="qlcs2">>0-3km ThetaE diff/Shear Vec & MLCAPE</div>
                </div>
            </div>

            <div class="divider" id="section_wpc">
                <div class="row">
                    <div class="row">
                        <div class="col-sm-2 image" id="pwtr">PWAT</div>
                        <div class="col-sm-2 image" id="tran_925">925 Moist Trans</div>
                        <div class="col-sm-2 image" id="tran">850 Moist Trans</div>
                        <div class="col-sm-2 image" id="tran_925-850">925-850 Mtrans</div>
                        <div class="col-sm-2 image" id="prop">Propagation Vec</div>
                        <div class="col-sm-2 image" id="peff">Pcpn Potential</div>
                    </div>

                    <div class="row">
                        <div class="col-sm-2 time">6 Hrly</div>
                        <div class="col-sm-2 image" id="hr61_qpf">t1</div>
                        <div class="col-sm-2 image" id="hr62_qpf">t2</div>
                        <div class="col-sm-2 image" id="hr63_qpf">t3</div>
                        <div class="col-sm-2 image" id="hr64_qpf">t4</div>
                        <div class="col-sm-2 image" id="hr65_qpf">t5</div>
                    </div>
                    <div class="row">
                        <div class="col-sm-2 time">Daily QPF</div>
                        <div class="col-sm-2 image" id="dy1_qpf">Day 1</div>
                        <div class="col-sm-2 image" id="dy2_qpf">Day 2</div>
                        <div class="col-sm-2 image" id="dy3_qpf">Day 3</div>
                        <div class="col-sm-2 image" id="dy45_qpf">Days 4-5</div>
                    </div>
                    <div class="row">
                        <div class="col-sm-2 time">Combined QPF</div>
                        <div class="col-sm-2 image" id="dy12_qpf">Days 1-2</div>
                        <div class="col-sm-2 image" id="dy13_qpf">Days 1-3</div>
                        <div class="col-sm-2 image" id="dy15_qpf">Days 1-5</div>
                        <div class="col-sm-2 image" id="dy17_qpf">Days 1-7</div>
                    </div>
                    <div class="row">
                        <div class="col-sm-2 time">Outlooks</div>
                        <div class="col-sm-2 image" id="dy1_exp">Day 1</div>
                        <div class="col-sm-2 image" id="dy2_exp">Day 2</div>
                        <div class="col-sm-2 image" id="dy3_exp">Day 3</div>
                        <div class="col-sm-2 image" id="md_exp">MD</div>
                    </div>
                </div>
            </div>

            <div class="divider" id="section_ma-winter">
                <div class="row">
                    <div class="col-sm-2 image nr" id="ptyp">Precipitation Type</div>
                    <div class="col-sm-2 image nr" id="epvl">800-750mb EPVg</div>
                    <div class="col-sm-2 image nr" id="epvm">650-500mb EPVg</div>
                    <div class="col-sm-2 image nr" id="les1">Lake Effect Snow 1</div>
                    <div class="col-sm-2 image nr" id="les2">Lake Effect Snow 2</div>
                    <div class="col-sm-2 image nr" id="snsq">Snow Squall Parameter</div>
                    <div class="col-sm-2 image nr" id="dend">Dendritic Growth Layer Depth</div>
                    <div class="col-sm-2 image nr" id="dendrh">Dendritic Growth Layer RH</div>
                </div>
            </div>

            <div class="divider" id="section_ma-fire">
                <div class="row">
                    <div class="col-sm-2 image nr" id="sfir">Sfc RH / T / Wind</div>
                    <div class="col-sm-2 image nr" id="fosb">Fosberg Index</div>
                    <div class="col-sm-2 image nr" id="lhan">Low Haines Index</div>
                    <div class="col-sm-2 image nr" id="mhan">Mid Haines Index</div>
                    <div class="col-sm-2 image nr" id="hhan">High Haines Index</div>
                    <div class="col-sm-2 image nr" id="lasi">Lower Atmos Severity Index</div>
                </div>
            </div>

            <div class="divider" id="section_sounding">
                <div class="row">
                    <div class="col-sm-1 image" id="ABQ">ABQ</div>
                    <div class="col-sm-1 image" id="ABR">ABR</div>
                    <div class="col-sm-1 image" id="ALY">ALY</div>
                    <div class="col-sm-1 image" id="AMA">AMA</div>
                    <div class="col-sm-1 image" id="APX">APX</div>
                    <div class="col-sm-1 image" id="BIS">BIS</div>
                    <div class="col-sm-1 image" id="BMX">BMX</div>
                    <div class="col-sm-1 image" id="BNA">BNA</div>
                    <div class="col-sm-1 image" id="BOI">BOI</div>
                    <div class="col-sm-1 image" id="BRO">BRO</div>
                    <div class="col-sm-1 image" id="BUF">BUF</div>
                    <div class="col-sm-1 image" id="CAR">CAR</div>
                    <div class="col-sm-1 image" id="CHH">CHH</div>
                    <div class="col-sm-1 image" id="CHS">CHS</div>
                    <div class="col-sm-1 image" id="CRP">CRP</div>
                    <div class="col-sm-1 image" id="DDC">DDC</div>
                    <div class="col-sm-1 image" id="DNR">DNR</div>
                    <div class="col-sm-1 image" id="DRT">DRT</div>
                    <div class="col-sm-1 image" id="DTX">DTX</div>
                    <div class="col-sm-1 image" id="DVN">DVN</div>
                    <div class="col-sm-1 image" id="EPZ">EPZ</div>
                    <div class="col-sm-1 image" id="EYW">EYW</div>
                    <div class="col-sm-1 image" id="FFC">FFC</div>
                    <div class="col-sm-1 image" id="FGZ">FGZ</div>
                    <div class="col-sm-1 image" id="FWD">FWD</div>
                    <div class="col-sm-1 image" id="GGW">GGW</div>
                    <div class="col-sm-1 image" id="GJT">GJT</div>
                    <div class="col-sm-1 image" id="GRB">GRB</div>
                    <div class="col-sm-1 image" id="GSO">GSO</div>
                    <div class="col-sm-1 image" id="GYX">GYX</div>
                    <div class="col-sm-1 image" id="IAG">IAG</div>
                    <div class="col-sm-1 image" id="ILN">ILN</div>
                    <div class="col-sm-1 image" id="ILX">ILX</div>
                    <div class="col-sm-1 image" id="INL">INL</div>
                    <div class="col-sm-1 image" id="JAN">JAN</div>
                    <div class="col-sm-1 image" id="JAX">JAX</div>
                    <div class="col-sm-1 image" id="LBF">LBF</div>
                    <div class="col-sm-1 image" id="LCH">LCH</div>
                    <div class="col-sm-1 image" id="LIX">LIX</div>
                    <div class="col-sm-1 image" id="LKN">LKN</div>
                    <div class="col-sm-1 image" id="LZK">LZK</div>
                    <div class="col-sm-1 image" id="MAF">MAF</div>
                    <div class="col-sm-1 image" id="MFL">MFL</div>
                    <div class="col-sm-1 image" id="MFR">MFR</div>
                    <div class="col-sm-1 image" id="MHX">MHX</div>
                    <div class="col-sm-1 image" id="MPX">MPX</div>
                    <div class="col-sm-1 image" id="NKX">NKX</div>
                    <div class="col-sm-1 image" id="OAK">OAK</div>
                    <div class="col-sm-1 image" id="OAX">OAX</div>
                    <div class="col-sm-1 image" id="OKX">OKX</div>
                    <div class="col-sm-1 image" id="OTX">OTX</div>
                    <div class="col-sm-1 image" id="OUN">OUN</div>
                    <div class="col-sm-1 image" id="PBZ">PBZ</div>
                    <div class="col-sm-1 image" id="REV">REV</div>
                    <div class="col-sm-1 image" id="RIW">RIW</div>
                    <div class="col-sm-1 image" id="RNK">RNK</div>
                    <div class="col-sm-1 image" id="SGF">SGF</div>
                    <div class="col-sm-1 image" id="SHV">SHV</div>
                    <div class="col-sm-1 image" id="SLC">SLC</div>
                    <div class="col-sm-1 image" id="SLE">SLE</div>
                    <div class="col-sm-1 image" id="TAE">TAE</div>
                    <div class="col-sm-1 image" id="TBW">TBW</div>
                    <div class="col-sm-1 image" id="TFX">TFX</div>
                    <div class="col-sm-1 image" id="TOP">TOP</div>
                    <div class="col-sm-1 image" id="TUS">TUS</div>
                    <div class="col-sm-1 image" id="UIL">UIL</div>
                    <div class="col-sm-1 image" id="UNR">UNR</div>
                    <div class="col-sm-1 image" id="VEF">VEF</div>
                    <div class="col-sm-1 image" id="WAL">WAL</div>
                </div>
            </div>

            <div class="divider" id="section_radar">
                <div class="row">
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-conus">CONUS</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-se">Southeast US</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-nw">Northwest US</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-sr">Southern Rockies</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-nr">Northern Rockies</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-umv">Upper MS Valley</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-smv">Southern MS Valley</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-sp">Southern Plains</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-cgl">Central Great Lakes</div>
                    <div class="col-sm-2 image sector-radar-loop nr" id="rl-ne">Northeast US</div>
                </div>
            </div>


            <div class="divider" id="section_satellite">
                <div class="row">
                    <div class="col-sm-2 image us-loop" id="conus-ch02">CONUS Vis</div>
                    <div class="col-sm-2 image us-loop" id="conus-ch13">CONUS Clean IR</div>
                    <div class="col-sm-2 image us-loop" id="conus-sand">CONUS Sandwich</div>
                    <div class="col-sm-2 image us-loop" id="conus-ch08">CONUS Upper WV</div>
                    <div class="col-sm-2 image us-loop" id="conus-geoc">CONUS GeoColor</div>
                    <div class="col-sm-2 image us-loop" id="conus-airm">CONUS Airmass</div>

                    <div class="col-sm-2 image sector-loop" id="ch02">Sector Vis</div>
                    <div class="col-sm-2 image sector-loop" id="ch13">Sector Clean IR</div>
                    <div class="col-sm-2 image sector-loop" id="sand">Sector Sandwich</div>
                    <div class="col-sm-2 image sector-loop" id="ch08">Sector Upper WV</div>
                    <div class="col-sm-2 image sector-loop" id="geoc">Sector GeoColor</div>
                    <div class="col-sm-2 image sector-loop" id="airm">Sector Airmass</div>

                    <div class="col-sm-2 image" id="ch02i">CH02</div>
                    <div class="col-sm-2 image" id="ch13i">CH13</div>
                    <div class="col-sm-2 image us-loop" id="cint">Conv Init (image)</div>
                    <div class="col-sm-2 image" id="ch08i">CH08</div>
                    <div class="col-sm-2 image" id="ch09i">CH09</div>
                    <div class="col-sm-2 image" id="ch10i">CH10</div>
                    <div class="col-sm-2 image us-loop" id="conus-glm">CONUS GLM</div>
                    <div class="col-sm-2 image us-loop" id="conus-ch07">CONUS Near IR</div>
                    <div class="col-sm-2 image us-loop" id="conus-dayp">CONUS Day Phase</div>


                    <div class="col-sm-2 image us-loop" id="conus-nmic">CONUS Night Micro</div>
                    <div class="col-sm-2 image us-loop" id="conus-firt">CONUS Fire Temp</div>
                    <div class="col-sm-2 image" id="ch14i">CH14</div>
                    <div class="col-sm-2 image sector-loop" id="glm">Sector GLM</div>

                    <div class="col-sm-2 image sector-loop" id="ch07">Sector Near IR</div>
                    <div class="col-sm-2 image sector-loop" id="dayp">Sector Day Phase</div>
                    <div class="col-sm-2 image" id="ch01i">CH01</div>
                    <div class="col-sm-2 image" id="ch03i">CH03</div>
                    <div class="col-sm-2 image" id="ch04i">CH04</div>
                    <div class="col-sm-2 image" id="ch05i">CH05</div>
                    <div class="col-sm-2 image" id="ch06i">CH06</div>
                    <div class="col-sm-2 image" id="ch07i">CH07</div>

                    <div class="col-sm-2 image" id="ch11i">CH11</div>
                    <div class="col-sm-2 image" id="ch12i">CH12</div>
                    <div class="col-sm-2 image" id="ch15i">CH15</div>
                    <div class="col-sm-2 image" id="ch16i">CH16</div>
                </div>
            </div>
            <div class="divider" id="section_links">
                <div class="row justify-content-left text-center">
                    <div class="col-sm-2"><a href="http://autumnsky.us/vad/" target="_blank">VWP Hodographs</a>
                    </div>
                    <div class="col-sm-2"><a href="https://mrms.nssl.noaa.gov/qvs/product_viewer/"
                            target="_blank">MRMS</a></div>
                    <div class="col-sm-2"><a href="https://iris.ncep.noaa.gov" target="_blank">IRIS</a></div>
                    <div class="col-sm-2"><a href="https://www.spc.noaa.gov/exper/href/" target="_blank">SPC HREF</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.spc.noaa.gov/exper/hrrr/" target="_blank">SPC HRRR</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.spc.noaa.gov/exper/sref/" target="_blank">SPC SREF</a>
                    </div>
                    <div class="col-sm-2"><a href="https://twitter.com/nadocast" target="_blank">NadoCast</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.tropicaltidbits.com/analysis/models/" target="_blank">Tropical Tidbits</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.pivotalweather.com/model.php" target="_blank">Pivotal</a>
                    </div>
                    <div class="col-sm-2"><a href="https://rapidrefresh.noaa.gov/hrrr/HRRR/Welcome.cgi?dsKey=hrrr_ncep_jet" target="_blank">GSD HRRR</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.spc.noaa.gov/exper/hrrr/sscram/index2.php"
                            target="_blank">SSCRAM</a>
                    </div>
                    <div class="col-sm-2"><a href="https://cbwofs.nssl.noaa.gov/Forecast"
                        target="_blank">WoFS</a>
                </div>
                    <div class="col-sm-2"><a href="https://www.eas.slu.edu/CIPS/SVRprob/SVRprob.php"
                            target="_blank">CIPS Severe Analogs</a>
                    </div>
                    <div class="col-sm-2"><a href="https://schumacher.atmos.colostate.edu/hilla/csu_mlp/index.php"
                            target="_blank">CSU ML Svr Probs</a>
                    </div>
                    <div class="col-sm-2"><a href="https://ncar.github.io/modeview/" target="_blank">NCAR HRRR Storm
                            Mode</a>
                    </div>
                    <div class="col-sm-2"><a href="https://www.spc.noaa.gov/exper/reports/" target="_blank">Interactive
                            LSRs</a>
                    </div>
                    <div class="col-sm-2"><a href="https://cimss.ssec.wisc.edu/severe_conv/psv3.html"
                            target="_blank">ProbSevere3</a>
                    </div>
                    <div class="col-sm-2"><a href="https://cimss.ssec.wisc.edu/severe_conv/pltg.html"
                            target="_blank">LightningCast</a>
                    </div>
                    <div class="col-sm-2"><a href="http://arctic.som.ou.edu/tburg/products/R2O/torprob/"
                            target="_blank">Tor Prob</a>
                    </div>
                    <div class="col-sm-2"><a
                            href="https://www.lightningmaps.org/?lang=en#t=3;s=0;o=0;b=;ts=0;m=oss;y=40.8162;x=-93.6011;z=6;d=2;dl=2;dc=0"
                            target="_blank">Ltg Maps</a>
                    </div>
                    <div class="col-sm-2"><a
                            href="https://rammb-slider.cira.colostate.edu/?sat=goes-16&z=3&im=12&ts=1&st=0&et=0&speed=130&motion=loop&map=1&lat=0&opacity%5B0%5D=1&hidden%5B0%5D=0&pause=0&slider=-1&hide_controls=0&mouse_draw=0&follow_feature=0&follow_hide=0&s=rammb-slider&sec=conus&p%5B0%5D=cira_glm_l2_group_counts&x=5056&y=3129"
                            target="_blank">GLM</a>
                    </div>
                    <div class="col-sm-2"><a
                            href="https://sites.google.com/view/nws-acars-sounding-page/acars-national-page"
                            target="_blank">ACARS Sounding</a>
                    </div>
                    <div class="col-sm-2"><a
                            href="https://noaa.maps.arcgis.com/apps/opsdashboard/index.html#/c6b6620afa4844fe977bc662e63b0949?"
                            target="_blank">HydroViewer AGOL</a>
                    </div>
                    <div class="col-sm-2"><a
                            href="https://noaa.maps.arcgis.com/apps/opsdashboard/index.html#/51dd128593384741a90b9a63609c2394"
                            target="_blank">IDSS Dashboard</a>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="container-fluid">
        <div class="d-flex justify-content-center text-center">
            <div class="row fit">
                <img id="display-image" class="img-fluid display-image"
                    src="https://www.spc.noaa.gov/products/outlook/day1otlk.gif">
            </div>
        </div>
    </div>
    <div class="container-fluid">
        <div class="d-flex justify-content-center text-left description box">
            <div class="row">
                <div id="describe">Click product for description
                </div>
            </div>
        </div>
    </div>

    <!---------------------------------------------------------------------------------------------------
    ------------------------------------ SCRIPTS --------------------------------------------------------
    ----------------------------------------------------------------------------------------------------->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
    <script>
        const spc_prods = 'https://www.spc.noaa.gov/products/'
        const spc_out = spc_prods + 'outlook/'
        const day1prob = spc_out + 'day1probotlk_'
        const day2prob = spc_out + 'day2probotlk_'

        let ma_sector = 's21'
        const exper = 'http://www.spc.noaa.gov/exper/'
        let ma_base = exper + 'mesoanalysis/'
        let ma = ma_base + ma_sector + '/'

        const wpc_qpf = 'http://www.wpc.ncep.noaa.gov/qpf/'
        const sat = 'https://cdn.star.nesdis.noaa.gov//GOES16/ABI/SECTOR/';
        const sat_conus = 'https://cdn.star.nesdis.noaa.gov//GOES16/ABI/CONUS/'
        let urls = {
            'conus-glm': 'https://cdn.star.nesdis.noaa.gov/GOES16/GLM/CONUS/EXTENT3/GOES16-CONUS-EXTENT3-625x375.gif',
            'conus-geoc': sat_conus + 'GEOCOLOR/GOES16-CONUS-GEOCOLOR-625x375.gif',
            'conus-airm': sat_conus + 'AirMass/GOES16-CONUS-AirMass-625x375.gif',
            'conus-sand': sat_conus + 'Sandwich/GOES16-CONUS-Sandwich-625x375.gif',
            'conus-dayp': sat_conus + 'DayCloudPhase/GOES16-CONUS-DayCloudPhase-625x375.gif',
            'conus-nmic': sat_conus + 'NightMicrophysics/GOES16-CONUS-NightMicrophysics-625x375.gif',
            'conus-firt': sat_conus + 'FireTemperature/GOES16-CONUS-FireTemperature-625x375.gif',
            'conus-ch02': sat_conus + '02/GOES16-CONUS-02-625x375.gif',
            'conus-ch07': sat_conus + '07/GOES16-CONUS-07-625x375.gif',
            'conus-ch08': sat_conus + '08/GOES16-CONUS-08-625x375.gif',
            'conus-ch13': sat_conus + '13/GOES16-CONUS-13-625x375.gif',
            'glm': 'https://cdn.star.nesdis.noaa.gov/GOES16/GLM/SECTOR/cgl/EXTENT3/GOES16-CGL-EXTENT3-600x600.gif',
            'ch02': sat + 'CGL/02/GOES16-CGL-02-600x600.gif',
            'ch07': sat + 'CGL/07/GOES16-CGL-07-600x600.gif',
            'ch08': sat + 'CGL/08/GOES16-CGL-08-600x600.gif',
            'ch13': sat + 'CGL/13/GOES16-CGL-13-600x600.gif',
            'ch14': sat + 'CGL/14/GOES16-CGL-14-600x600.gif',
            'ch07': sat + 'CGL/07/GOES16-CGL-07-600x600.gif',
            'geoc': sat + 'CGL/GEOCOLOR/GOES16-CGL-GEOCOLOR-600x600.gif',
            'airm': sat + 'CGL/AirMass/GOES16-CGL-AirMass-600x600.gif',
            'sand': sat + 'CGL/Sandwich/GOES16-CGL-Sandwich-600x600.gif',
            'dayp': sat + 'CGL/DayCloudPhase/GOES16-ABI-CGL-DayCloudPhase-600x600.gif',
            'nmic': sat + 'CGL/NightMicrophysics/GOES16-CGL-NightMicrophysics-600x600.gif',
            'geoci': sat + 'CGL/GEOCOLOR/GOES16-CGL-GEOCOLOR-600x600.gif',
            'airmi': sat + 'CGL/AirMass/GOES16-CGL-AirMass-600x600.gif',
            'sandi': sat + 'CGL/Sandwich/600x600.jpg',
            'dmici': sat + 'CGL/DayCloudPhase/600x600.jpg',
            'nmici': sat + 'CGL/NightMicrophysics/600x600.jpg',
            'ch01i': sat + 'CGL/01/600x600.jpg',
            'ch02i': sat + 'CGL/02/600x600.jpg',
            'ch03i': sat + 'CGL/03/600x600.jpg',
            'ch04i': sat + 'CGL/04/600x600.jpg',
            'ch05i': sat + 'CGL/05/600x600.jpg',
            'ch06i': sat + 'CGL/06/600x600.jpg',
            'ch07i': sat + 'CGL/07/600x600.jpg',
            'ch08i': sat + 'CGL/08/600x600.jpg',
            'ch09i': sat + 'CGL/09/600x600.jpg',
            'ch10i': sat + 'CGL/10/600x600.jpg',
            'ch11i': sat + 'CGL/11/600x600.jpg',
            'ch12i': sat + 'CGL/12/600x600.jpg',
            'ch13i': sat + 'CGL/13/600x600.jpg',
            'ch14i': sat + 'CGL/14/600x600.jpg',
            'ch15i': sat + 'CGL/15/600x600.jpg',
            'ch16i': sat + 'CGL/16/600x600.jpg',
            'rpts': 'https://www.spc.noaa.gov/climo/reports/today.gif',
            'dy1_otlk': spc_out + 'day1otlk.gif',
            'dy1_hail': day1prob + 'hail.gif',
            'dy1_wind': day1prob + 'wind.gif',
            'dy1_torn': day1prob + 'torn.gif',
            'dy3_otlk': spc_out + 'day3otlk.gif',
            'dy1_0100_otlk': spc_out + 'day1otlk_0100.gif',
            'dy1_0100_torn': day1prob + '0100_torn.gif',
            'dy1_0100_hail': day1prob + '0100_hail.gif',
            'dy1_0100_wind': day1prob + '0100_wind.gif',
            'dy1_0600_otlk': spc_out + 'day1otlk_1200.gif',
            'dy1_0600_torn': day1prob + '1200_torn.gif',
            'dy1_0600_hail': day1prob + '1200_hail.gif',
            'dy1_0600_wind': day1prob + '1200_wind.gif',
            'dy1_1300_otlk': spc_out + 'day1otlk_1300.gif',
            'dy1_1300_torn': day1prob + '1300_torn.gif',
            'dy1_1300_hail': day1prob + '1300_hail.gif',
            'dy1_1300_wind': day1prob + '1300_wind.gif',
            'dy1_1630_otlk': spc_out + 'day1otlk_1630.gif',
            'dy1_1630_torn': day1prob + '1630_torn.gif',
            'dy1_1630_hail': day1prob + '1630_hail.gif',
            'dy1_1630_wind': day1prob + '1630_wind.gif',
            'dy1_2000_otlk': spc_out + 'day1otlk_2000.gif',
            'dy1_2000_torn': day1prob + '2000_torn.gif',
            'dy1_2000_hail': day1prob + '2000_hail.gif',
            'dy1_2000_wind': day1prob + '2000_wind.gif',
            'dy2_otlk': spc_out + 'day2otlk.gif',
            'dy2_torn': spc_out + 'day2probotlk_torn.gif',
            'dy2_wind': spc_out + 'day2probotlk_wind.gif',
            'dy2_hail': spc_out + 'day2probotlk_hail.gif',
            'dy2_0600_otlk': spc_out + 'day2otlk_0600_prt.gif',
            'dy2_0600_torn': spc_out + 'day2probotlk_0600_torn_prt.gif',
            'dy2_0600_hail': spc_out + 'day2probotlk_0600_hail_prt.gif',
            'dy2_0600_wind': spc_out + 'day2probotlk_0600_wind_prt.gif',
            'dy2_1730_otlk': spc_out + 'day2otlk_1730_prt.gif',
            'dy2_1730_torn': spc_out + 'day2probotlk_1730_torn_prt.gif',
            'dy2_1730_hail': spc_out + 'day2probotlk_1730_hail_prt.gif',
            'dy2_1730_wind': spc_out + 'day2probotlk_1730_wind_prt.gif',
            'dy2_hail': spc_out + 'day2probotlk_hail.gif',
            'dy2_wind': spc_out + 'day2probotlk_wind.gif',
            'dy1_qpf': wpc_qpf + 'fill_94qwbg.gif',
            'dy2_qpf': wpc_qpf + 'fill_98qwbg.gif',
            'dy3_qpf': wpc_qpf + 'fill_99qwbg.gif',
            'dy45_qpf': wpc_qpf + '95ep48iwbg_fill.gif',
            'dy67_qpf': wpc_qpf + '97ep48iwbg_fill.gif',
            'dy12_qpf': wpc_qpf + 'd12_fill.gif',
            'dy13_qpf': wpc_qpf + 'd13_fill.gif',
            'dy15_qpf': wpc_qpf + 'p120i.gif',
            'dy17_qpf': wpc_qpf + 'p168i.gif',
            'dy1_exp': wpc_qpf + '94ewbg.gif',
            'dy2_exp': wpc_qpf + '98ewbg.gif',
            'dy3_exp': wpc_qpf + '99ewbg.gif',
            'md_exp': 'https://www.wpc.ncep.noaa.gov/metwatch/latest_mdmap.gif',
            'hr61_qpf': wpc_qpf + 'fill_91ewbg.gif',
            'hr62_qpf': wpc_qpf + 'fill_92ewbg.gif',
            'hr63_qpf': wpc_qpf + 'fill_93ewbg.gif',
            'hr64_qpf': wpc_qpf + 'fill_9eewbg.gif',
            'hr65_qpf': wpc_qpf + 'fill_9fewbg.gif',
            's-watch': spc_prods + 'watch/validww.png',
            's-mds': spc_prods + 'md/validmd.gif',
            'cint': 'https://www.nsstc.uah.edu/SATCAST/goes-east_fulldomain/UAH_SATCASTv3_CI_VIS.png'
        }


        let spc_items = ['eshr', 'shr6', 'shr8', 'shr3', 'shr1', 'brns', 'effh', 'srh3', 'srh1', 'srh5', 'llsr',
            'mlsr', 'ulsr', 'alsr', 'mnwd', 'xover', 'srh3_chg', 'shr1_chg', 'shr6_chg', 'hodo', 'sbcp', 'mlcp',
            'mucp', 'eltm', 'ncap', 'dcape', 'laps', 'muli', 'lllr', 'maxlr', 'lclh', 'lcls', 'lfch', 'lfrh',
            'sbcp_chg', 'sbcn_chg', 'mlcp_chg', 'mucp_chg', 'lllr_chg', 'laps_chg', 'skewt', 'ttot', 'show', 'kidx',
            'hail', 'sars1', 'sars2', 'lghl', 'dcp', 'mbcp', 'qlcs1', 'qlcs2', 'scp', 'lscp', 'stor', 'stpc',
            'stpc5', 'sigt1', 'sigt2', 'nstp', 'vtp3', 'sigh', 'cbsig', 'cpsh', 'vgp3',
            'lcls', 'lr3c', '3cvr', '3cape_shr3', '925mb', '850mb', '850mb2', '700mb', '500mb', '300mb', 'tran',
            'dlcp', 'tadv_925', 'tadv', '7tad', '9fnt', '8fnt', '7fnt', '857f', '75ft', '98ft', 'vadv', 'ageo',
            'sfnt', '925f', '500mb_chg', 'nstp', 'cpsh', 'lr3c', 'pwtr', 'tran', 'prop', 'peff',
            'tran_925', 'tran_925-850', 'bigsfc', 'pmsl', 'ttd', 'mcon', 'mxth', 'thea', 'thet', 'icon', 'trap',
            'vtm', 'dvvr', 'def', 'sfnt', 'pchg', 'temp_chg', 'dwpt_chg', 'mixr_chg', 'thte_chg', '925mb', '850mb',
            '700mb', '500mb', '300mb', 'tadv_925', 'tadv', '7tad', 'ddiv', 'padv', 'brn', 'desp', 'ehi1', 'ehi3',
            'vgp3', 'crit', 'mlcape_eshr', 'comp', 'lcls', 'tdlr', 'mcsm', 'mbcp', 'sfir', 'fosb', 'lhan', 'mhan',
            'hhan', 'lasi', 'trap_500', 'trap_250', 'sherbe', 'moshe', 'cwasp', 'tehi', 'tts', 'ptstpe', 'pstpe',
            'pvstpe', 'snsq', 'ptyp', 'epvl', 'epvm', 'les1', 'les2', 'dend', 'dendrh'
        ]

        spc_items.forEach(s => {
            urls[s] = ma + s + '/' + s + '.gif'
        });


        /////////////////////////////////////////////////////////////

        function soundingDate() {
            // create a new timestamp 
            var now = new Date();

            var year = now.getUTCFullYear().toString().slice(-2)
            var month = now.getUTCMonth() + 1;
            monstr = month.toString();
            if (monstr.length == 1) {
                monstr = '0' + monstr;
            }
            var date = now.getUTCDate().toString();
            if (date.length == 1) {
                date = '0' + date
            }
            var hour = now.getUTCHours();
            if (hour > 12) {
                var hr = '12'
            } else {
                var hr = '00'
            }

            let dateString = year + monstr + date + hr + '_OBS/';
            return dateString;
        }

        const sound = exper + 'soundings/'
        let soundDate = soundingDate();

        const soundings = ['UIL', 'OTX', 'SLE', 'MFR', 'BOI', 'TFX', 'GGW', 'RIW', 'SLC', 'LKN', 'REV', 'OAK', 'VEF',
            'GJT', 'FGZ', 'NKW', 'TUS', 'ABQ', 'EPZ', 'DRT', 'MAF', 'AMA', 'OUN', 'DDC', 'TOP', 'LBF', 'OAX', 'RAP',
            'ABR', 'BIS', 'INL', 'MPX', 'GRB', 'DVN', 'ILX', 'SGF', 'LZK', 'SHV', 'LCH', 'JAN', 'LIX', 'APX', 'DTX',
            'ILN', 'BNA', 'BMX', 'FFC', 'BUF', 'PIT', 'EVW', 'MFL', 'TBW', 'JAX', 'CHS', 'MHX', 'GSC', 'RNK', 'PIT',
            'IAG', 'WAL', 'OKX', 'ALB', 'GYX'
        ]

        soundings.forEach(sounding => {
            urls[sounding] = sound + soundDate + sounding + '.gif'

        })
        ////////////////////////////////////////////////////////////

        const images = document.querySelectorAll("div.image");
        const buttons = document.querySelectorAll("button");
        const dividers = document.querySelectorAll(".divider");
        const radios = document.querySelectorAll(".radio");
        const radar_loops = ['rl-conus', 'rl-nw', 'rl-nr', 'rl-sr', 'rl-umv', 'rl-sp', 'rl-cgl', 'rl-ne', 'rl-se', 'rl-smv']
        const sat_loops = ['ch02', 'ch07', 'ch08', 'ch13', 'ch14', 'geoc', 'airm', 'sand', 'nmic', 'dayp', 'firt']
        const sat_images = ['ch01i', 'ch02i', 'ch03i', 'ch04i', 'ch05i', 'ch06i', 'ch07i', 'ch08i', 'ch09i', 'ch10i',
            'ch11i', 'ch12i', 'ch13i', 'ch14i', 'ch15i', 'ch16i'
        ]

        const radar_loop_names = {
            'rl-conus': 'CONUS-LARGE',
            'rl-nw': 'PACNORTHWEST',
            'rl-nr': 'NORTHROCKIES',
            'rl-sr': 'SOUTHROCKIES',
            'rl-umv': 'UPPERMISSVLY',
            'rl-sp': 'SOUTHPLAINS',
            'rl-cgl': 'CENTGRLAKES',
            'rl-ne': 'NORTHEAST',
            'rl-se': 'SOUTHEAST',
            'rl-smv': 'SOUTHMISSVLY',
            //'s18': 'smv',
        }

        const sat_loop_names = {
            'ch02': '02',
            'ch07': '07',
            'ch08': '08',
            'ch13': '13',
            'ch14': '14',
            'geoc': 'GEOCOLOR',
            'airm': 'AirMass',
            'sand': 'Sandwich',
            'dayp': 'DayCloudPhase',
            'nmic': 'NightMicrophysics',
            'firt': 'FireTemperature'
        }

        const sat_sector = {
            's11nw': 'pnw',
            's11nr': 'nr',
            's12sw': 'psw',
            's12sr': 'sr',
            's13': 'umv',
            's20': 'umv',
            's14': 'sp',
            's15': 'sp',
            's16gl': 'cgl',
            's16ne': 'ne',
            's17': 'se',
            's18se': 'se',
            's18smv': 'smv',
            's21gl': 'cgl',
            //'s18': 'smv',
        }


        function getImage(e) {
            reference_id = e.target.id
            imgURL = urls[reference_id]
            desc = descriptions[reference_id]
            newURL = refreshImage(imgURL);
            document.getElementById(reference_id).classList.add('highlight');
            document.getElementById('display-image').src = newURL;
        }


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

        function removeHighlight(e) {
            reference_id = e.target.id
            document.getElementById(e.target.id).classList.remove('highlight');
        }

        function refreshImage(imgURL) {
            // create a new timestamp 
            var timestamp = new Date().getTime();
            var queryString = "?t=" + timestamp;
            newSrc = imgURL + queryString;
            return newSrc
        }

        function adjustDividers(b) {
            dividers.forEach(divider => {
                divider.style.display = 'none';
            })

            document.getElementById('describe').innerHTML = 'none';

            let new_reference_id = "section_" + b.target.id
            //console.log(new_reference_id);
            document.getElementById(new_reference_id).style.display = 'block';
            if ((b.target.id === "links") || (b.target.id === "sounding") || (b.target.id === "swody1") || (b.target.id === "swody2") || (b.target.id === "spc_watch") || (b.target.id === "radar") ) {
                document.getElementById('instructions').style.display = 'none';
                document.getElementById('describe').innerHTML = 'No descriptions are available for this category.';      
            } else {
                document.getElementById('instructions').style.display = 'block';
                document.getElementById('describe').innerHTML = 'Click products for descriptions.';          
            }
        };

        function showSelected(e) {

            reference_id = e.target.id
            let m_sector = reference_id.slice(0, 3);
            let sat_sector_name = sat_sector[reference_id];
            let sat_sector_name_upper = sat_sector_name.toUpperCase();

            spc_items.forEach(s => {
                urls[s] = ma_base + m_sector + '/' + s + '/' + s + '.gif'
            });
            sat_images.forEach(image => {
                let channel = image.slice(2, -1);
                urls[image] = sat + sat_sector_name_upper + '/' + channel + '/600x600.jpg';
            });

            sat_loops.forEach(loop => {
                let loop_name = sat_loop_names[loop];
                urls[loop] = sat + sat_sector_name_upper + '/' + loop_name + '/GOES16-' +
                    sat_sector_name_upper + '-' + loop_name + '-600x600.gif';
            });

            urls['glm'] = 'https://cdn.star.nesdis.noaa.gov/GOES16/GLM/SECTOR/' + sat_sector_name +
                '//EXTENT3/GOES16-' + sat_sector_name_upper + '-EXTENT3-600x600.gif';

        };


        radar_loops.forEach(rl => {
                let rl_name = radar_loop_names[rl];
                urls[rl] = 'https://radar.weather.gov/ridge/lite/' + rl_name + '_loop.gif';
                console.log(urls[rl]);
            });


        for (const radio of radios) {
            radio.addEventListener('change', showSelected);
        };

        images.forEach(image => {
            image.addEventListener('mouseenter', e => {
                getImage(e);
            })

        });

        images.forEach(image => {
            image.addEventListener('click', c => {
                document.getElementById('instructions').style.display = 'none';
                getDescription(c);
            })

        });

        images.forEach(image => {
            image.addEventListener('mouseleave', l => {
                removeHighlight(l);
            })

        });

        buttons.forEach(btn => {
            btn.addEventListener('click', b => {

                adjustDividers(b);
            })

        });

        dividers.forEach(divider => {
            divider.style.display = 'none';
        });

        var descriptions = {

            'trap': '<div class="spc-prod">Fluid Trapping Parameter</div><div class="spc-info">In regions of strong vorticity \
            (i.e., cyclones), air parcels tend to become trapped within the vortex.  This can produce a boundary within which air \
            parcels are trapped and so follow the vortex over extended periods. In regions with strong deformation, some air parcels are \
            brought closer together but others become increasingly separated.  The trapping parameter (TRAP) is defined according to the simple \
            formula:  TRAP = 1/4 [(DEFres)^2 - (VOR)^2]. Negative values are identified regions where the vorticity is larger than the deformation, \
            and it is within such regions that air parcels are likely to be trapped. This parameter is useful for identifying the development \
            of strong vortices and for tracking them. <div class="spc-ref">Reference: Cohen, R. A., and D. M. Schultz, 2005: Contraction rate and \
            its relationship to frontogenesis, the Lyapunov exponent, fluid trapping, and airstream boundaries, <i>Mon. Wea. Rev.</i>, \
            <b>133</b>, 1353-1369.</div>',

            'td': '<div class="spc-prod">Surface</div><div class="spc-info">Temperature (solid purple &lt; 32 F, \
            solid brown &lt; 60 F, solid red > 60 F), Dewpoint (dashed blue, values > 56F shaded), and Pressure (solid black).</div>',

            'mcon': '<div class="spc-prod">Surface Moisture Convergence (solid blue) and Mixing Ratio (solid green).</div>',

            'mxth': '<div class="spc-prod">Surface Mixing Ratio (dashed blue > 6 g/kg, values > 9 shaded), Theta (solid red in K), and Wind.</div>',

            'thea': '<div class="spc-prod">Surface Theta-e, Theta-e Advection (+ values solid purple), and Wind.</div>',

            'icon': '<div class="spc-prod">Instantaneous Contraction Rate</div><div class="spc-info">\
            SPC Documentation <b><a href="https://www.spc.noaa.gov/exper/mesoanalysis/help/help_icon.html" \
            target="_blank">HERE</a></b></div>',

            'sfnt': '<div class="spc-prod">Surface Frontogenesis (solid red), Temperature (dashed blue in deg F), Pressure (solid black), and Wind.</div>',

            'temp_chg': '<div class="spc-prod">3-Hr Temperature Change</div><div class="spc-info">Temperature Change (solid black) and Wind. Values > \
            4 C shaded red (warmer); &lt; -4 shaded blue (cooler).</div>',

            'dwpt_chg': '<div class="spc-prod">3-Hr Dewpoint Change</div><div class="spc-info">Dewpoint Change (solid black) and Wind. Values > \
            4 C shaded green (moister); &lt; -4 shaded orange/brown (drier).</div>',

            'thte_chg': '<div class="spc-prod">3-Hr Theta-e Change</div><div class="spc-info">Theta-e Change (solid black) and Wind. Values \
            > 4 shaded green (warmer and/or moister); &lt; -4 shaded blue (cooler and/or drier).</div>',

            //  Upper

            '850mb': '<div class="spc-prod">850 mb</div><div class="spc-info"> Height (solid black), Temperature (dashed red > 0 C, dashed \
            blue &lt; 0 C), Dewpoint (solid green > 6 C), and Wind.</div>',

            '700mb': '<div class="spc-prod">700 mb</div><div class="spc-info"> Height (solid black), Temperature (dashed red > 0 C, dashed \
            blue &lt; 0 C), Wind, and 700-500 mb RH > 70 Pct (shaded).</div>',

            '500mb': '<div class="spc-prod">500 mb</div><div class="spc-info">Height (solid black), Temperature (dashed red), \
            Wind, and Isotachs (shaded > 40 kts).</div>',

            '300mb': '<div class="spc-prod">300 mb</div><div class="spc-info">Heights(solid black), Wind, Isotachs (shaded > \
            60 kts), and Divergence (solid magenta).</div>',

            'dlcp': '<div class="spc-prod">Deep Layer Moisture Flux Convergence and 100 mb Mean Mixing Ratio</div><div class="spc-info">\
            (solid red = CON; dashed blue = DIV) and 100 mb Mean Mixing Ratio (solid green > 6). High values = good moisture supply/replenishment \
            to MCS. New cell development may occur in/near max values associated with boundaries.</div>',

            'tadv_925': '<div class="spc-prod">925 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
            WAA; blue shade = CAA), Height (solid black), and Wind. 925 mb WAA = 925 mb (+) theta-e advection, if moisture is constant or \
            increasing, i.e., favorable location for convection, especially elevated convection.</div>',

            'tadv': '<div class="spc-prod">850 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
            WAA; blue shade = CAA), Height (solid black), and Wind. 850 mb WAA = 850 mb (+) theta-e advection, if moisture is constant or \
            increasing, i.e., favorable location for convection, especially elevated convection.</div>',

            '7tad': '<div class="spc-prod">700 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
            WAA; blue shade = CAA), Height (solid black), and Wind. Elevated convection may be within/near max in 700 mb WAA/700 mb (+) \
            theta-e advection.</div>',

            '7fnt': '<div class="spc-prod">700 mb Petterssen`s Frontogenesis</div><div class="spc-info">700 mb Petterssen`s Frontogenesis \
            (solid purple), Height (solid black), Temperature (dashed red), and Wind. Compare 850-700 frontogenesis axis to 700-500 axis \
            to determine depth and slope of frontogenetical surface. If they are nearly superimposed, then steep mesoscale lifting is \
            likely to promote banded precip and convection.</div>',

            'tadv_925': '<div class="spc-prod"> </div><div class="spc-info"></div>',

            '98ft': '<div class="spc-prod">925-850 mb Petterssen`s Frontogenesis</div><div class="spc-info">925-850 mb Petterssen`s \
            Frontogenesis(solid purple), Height (solid black), Temperature (dashed red), and Wind. Note that label below graphic \
            (925-700 mb) is wrong.',

            '857f': '<div class="spc-prod">850-700 mb Petterssen`s Frontogenesis (solid purple), Height (solid black), \Temperature \
            (dashed red), and Wind</div><div class="spc-info">. 850-700 mb Petterssen`s Frontogenesis (solid purple), Height (solid black), \
            Temperature (dashed red), and Wind Compare 850-700 frontogenesis axis to 700-500 axis to determine depth and slope of \
            frontogenetical surface. If they are nearly superimposed, then steep mesoscale lifting is likely to promote banded precip\
            and convection.</div>',

            '75ft': "700-500 mb Petterssen's Frontogenesis (solid purple), Height (solid black), Temperature (dashed blue), and Wind. \
            Compare 700-500 frontogenesis axis to 850-700 axis to determine depth and slope of frontogenetical surface. If they are \
            nearly superimposed, then steep mesoscale lifting is likely to promote banded precip and convection.",

            'epvl': "850 mb Frontogenesis (solid red), 850-700 mb EPV (blue shading = stable; red/green/purple shading = unstable), \
            and Conditional Instability (solid black). Look for max 850 mb frontogenesis coincident with or just downstream from (-) \
            EPV. Also consider 700 mb frontogenesis and frontal slope between the 2 levels. It is likely that (-) EPV may only appear \
            above 850 mb (even above 700 mb), especially in cool season and with a low-level frontal inversion.",

            'epvm': "700 mb Frontogensis (solid red), 650-500 mb EPV (blue shading = stable; red/green shading = unstable), and \
            Conditional Instability (solid black). Look for max 700 mb frontogenesis coincident with or just downstream from (-) EPV. \
            Also consider 850 mb frontogenesis and frontal slope between the 2 levels. Frontogenesis and (-) EPV may extend or be \
            located above 700 mb at times, especially in cool season.",

            'vadv': '<div class="spc-prod">700-400 mb Differential Vorticity Advection</div><div class="spc-info"> 700-400 mb Differential \
            Vorticity Advection (DVA) and 500 mb Height (solid black) and Vorticity (shaded). (+) DVA = solid blue. (-) DVA = dashed red. \
            (+) DVA promotes synoptic-scale (isentropic) lift, moisture and temperature advection and convergence, and destabilization.</div>',

            'padv': '<div class="spc-prod">400-250 mb Potential Vorticity Advection</div><div class="spc-info">Identifies depressions in the \
            tropopause by assessing PV in a fixed layer. Movement of these depressions induces vertical motion depending on the static stabilty \
            of the atmosphere. Positive Potential Vorticity Advection is fairly well correlated with forcing for upward vertical motion.</div>',

            'ddiv': '<div class="spc-prod">850-250mb Differential Divergence</div><div class="spc-info">Differential Divergence (fill) \
            850 mb convergence (red contours) and 250 mb divergence (purple contours). Shows larger scale mass adjustments resulting in \
            forced upward vertical motion. Large values result in rapid convective destabilization if low-level moisture is large.</div>',

            'ageo': '<div class="spc-prod">300 mb Height, Isotachs, Ageostrophic Wind, 700-500 mb Omega</div><div class="spc-info">300 \
            mb Height (solid black), Isotachs (shaded), Ageostrophic Wind, and 700-500 mb Omega. Ascent = solid magenta. Descent = dashed \
            red. Best locations for organized convection is anticyclonically-curved right entrance regions (QLCS/MCS) and exit regions of \
            mid-to-upper jet streaks (supercells).</div>',

            '500mb_chg': '<div class="spc-prod">12hr 500 mb Height Change</div><div class="spc-info">12hr 500 mb Height change \
            Shows areas where longer-term forcing for upward vertical motion has taken place, allowing for atmospheric destabilization.\
            </div>',

            // trap_500 and trap_250 set equal to trap

            // Thermodynamics

            'sbcp': '<div class="spc-prod">Surface-Based CAPE/CIN (J kg<sup>-1</sup>)</div><div class="spc-info">SBCAPE \
            (<u><b>S</b></u>urface-<u><b>B</b></u>ased <u><b>C</b></u>onvective<u><b>A</b></u>vailable <u><b>P</b></u>otential <u><b>E</b></u>nergy) \
            is a measure of instability in the troposphere.  This value represents the total amount of potential energy available to a parcel \
            of air originating at the surface and being lifted to its level of free convection (LFC). No parcel entrainment is considered. The CAPE and \
            CIN calculations use the virtual temperature correction. CIN (<u><b>C</b></u>onvective <u><b>IN</b></u>hibition) represents the "negative" \
            area on a sounding that must be overcome before storm initiation can occur.</div>',

            'mlcp': '<div class="spc-prod">100-mb Mixed Layer CAPE/CIN (J kg<sup>-1</sup>)</div><div class="spc-info">MLCAPE (<u><b>M</b></u>ixed \
            <u><b>L</b></u>ayer <u><b>C</b></u>onvective<u><b>A</b></u>vailable <u><b>P</b></u>otential <u><b>E</b></u>nergy) is a measure of \
            instability in the troposphere.  This value represents the mean potential energy conditions available to parcels of air located in the \
            lowest \ 100-mb when lifted to the level of free convection (LFC). No parcel entrainment is considered. The CAPE and CIN calculations \
            use the virtual temperature correction. CIN (<u><b>C</b></u>onvective <u><b>IN</b></u>hibition) represents the "negative" area on a \
            sounding that must be overcome before storm initiation can occur.</div>',

            'mucp': '<div class="spc-prod">Most Unstable CAPE (J kg<sup>-1</sup>) &amp LPL Height (m AGL)</div><div class="spc-info">MUCAPE \
            (<u><b>M</b></u>ost <u><b>U</b></u>nstable <u><b>C</b></u>onvective <u><b>A</b></u>vailable <u><b>P</b></u>otential \
            <u><b>E</b></u>nergy) is a measure of instability in the troposphere.  This value represents the total amount of potential energy \
            available to the maximum equivalent potential temperature (within the lowest 300-mb of the atmosphere) while being lifted to its \
            level of free convection (LFC). No parcel entrainment is considered. The CAPE and CIN calculations use the virtual temperature \
            correction. The LPL (<u><b>L</b></u>ifted <u><b>P</b></u>arcel <u><b>L</b></u>evel) allows for the determination of the height of \
            the most unstable parcel. This makes it easy to identify areas where the largest CAPE is "elevated."</div>',

            'eltm': '<div class="spc-prod">EL temperature, MUCAPE, and MUCIN</div><div class="spc-info">Equilibrium level (EL) temperature \
            and most-unstable (MU) parcel CAPE are utilized to identify areas of potential lightning production, while large MUCIN suggests \
            that deep convection is unlikely.  Charge separation and lightning production occur with sufficiently strong updrafts (represented \
            by MUCAPE) that extend into the mixed phase (both ice and water) region (represented by EL temperature). Thunderstorms become more \
            probable as MUCAPE increases to above 100 J kg<sup>-1</sup> with EL temperatures of -20 C or colder.</div>',

            'ncap': '<div class="spc-prod">Normalized CAPE (J kg<sup>-1</sup>)</div><div class="spc-info">The NCAPE (<u><b>N</b></u>ormalized \
            CAPE) is CAPE that is divided by the depth of the buoyancy layer (units of m s**-2).  Values near or less than .1 suggest a "tall, \
            skinny" CAPE profile with relatively weak parcel accelerations, while values closer to .3 to .4 suggest a "fat" CAPE profile with \
            large parcel accelerations possible. Normalized CAPE and lifed indicies are similar measures of instability.</div>',

            'dcape': '<div class="spc-prod">Downdraft CAPE (J kg<sup>-1</sup>)</div><div class="spc-info">The DCAPE (<u><b>D</b></u>owndraft CAPE) \
            can be used to estimate the potential strength of rain-cooled downdrafts within deep convection, and is similar to CAPE. Larger DCAPE \
            values are associated with stronger downdrafts.  Likewise, DCIN (downdraft inhibition) is analogous to convective inhibition (hatching \
            at 25 and 100 J kg<sup>-1</sup>)</div>',

            'muli': '<div class="spc-prod">Surface-Based Lifted Index (C) & Convective Inhibition (J kg-1)</div><div class="spc-info">SBLI (Surface \
            Based Lifted Index & Convective Inhibition) is the Lifted Index at 500-mb, based on the surface parcel, and the convective inhibition \
            for the same parcel. These fields are meant to identify areas of surface-based CAPE and minimal convective inhibition, which suggests \
            some threat for surface-based thunderstorms.</div>',

            'laps': '<div class="spc-prod">Mid-Level Lapse Rates (C km<sup>-1</sup>)</div><div class="spc-info">A lapse rate is the rate of temperature \
            change with height.  The faster the temperature decreases with height, the "steeper" the lapse rate and the more "unstable" the atmosphere \
            becomes. Lapse rates are shown in terms of degrees Celcius change per kilometer in height.  Values less than 5.5-6.0 C km<sup>-1</sup> \
            ("moist" adiabatic) represent "stable" conditions, while values greater than 9.8 C km<sup>-1</sup> ("dry" adiabatic) are considered \
            "absolutely unstable."  In between these two values, lapse rates are considered "conditionally unstable." Conditional instability means \
            that if enough moisture is present, lifted air parcels could have a negative LI (lifted index) or positive CAPE. The 700-500 mb lapse \
            rates, also referred to as mid-level lapse rates, are meant to identify regions where deep convection is more probable (all else being \
            equal).  Likewise, steeper lapse rates correspond to the possibility of larger CAPE and stronger storm updrafts.</div>',

            'lllr': '<div class="spc-prod">Low-Level Lapse Rates (C km<sup>-1</sup>)</div><div class="spc-info">A lapse rate is the rate of temperature \
            change with height.  The faster the temperature decreases with height, the "steeper" the lapse rate and the more "unstable" the atmosphere \
            becomes. Lapse rates are shown in terms of degrees Celcius change per kilometer in height.  Values less than 5.5-6.0 C km<sup>-1</sup>("moist" \
            adiabatic) represent "stable" conditions, while values greater than 9.8 C km<sup>-1</sup> ("dry" adiabatic) are considered "absolutely \
            unstable."  In between these two values, lapse rates are considered "conditionally unstable." Conditional instability means that if \
            enough moisture is present, lifted air parcels could have a negative LI (lifted index) or positive CAPE. The 0-3 km lapse rates, \
            also referred to as low-level lapse rates, are meant to identify regions of deeper mixing (e.g., steeper lapse rates) that often result \
            in weakening convective inhibition that precedes surface-based thunderstorm development, as well as the potential for strong downdrafts \
            in the low levels.</div>',

            'maxlr': '<div class="spc-prod">Max Lapse Rate</div><div class="spc-info">The maximum lapse rate (C km<sup>-1</sup>) in a 2 km deep \
            layer (incremented every 250 m in the vertical) from 2-6 km above ground level.</div>',

            'lclh': '<div class="spc-prod">Lifting Condensation Level (m AGL)</div><div class="spc-info">The LCL (<u><b>L</b></u>ifting \
            <u><b>C</b></u>ondensation <u><b>L</b></u>evel) is the level at which a parcel becomes saturated.  It is a reasonable estimate \
            of cloud base height when parcels experience forced ascent. The height difference between this parameter and the LFC is important \
            when determining convection initiation.  The smaller the difference between the LCL and the LFC, the more likely deep convection \
            becomes. The LFC-LCL difference is similar to CIN (convective inhibition).</div>',

            'lfch': '<div class="spc-prod">Level of Free Convection (m AGL)</div><div class="spc-info">The LFC (<u><b>L</b></u>evel of \
            <u><b>F</b></u>ree <u><b>C</b></u>onvection) is the level at which a lifted parcel begins a free acceleration upward to the \
            equilibrium level.  Recent preliminary research suggests that tornadoes become more likely in supercells when LFC heights are \
            less than 2000-m above ground level. The EL (equilibrium level) is the level at which a lifted parcel becomes cooler than the \
            environmental temperature and is no longer unstable.  The EL is used primarily to estimate the height of a thunderstorm \
            anvil. The height difference between this parameter and the LCL is important when determining convection initiation.  The smaller \
            the difference between the LFC and the LCL, the more likely deep convection becomes. The LFC-LCL difference is similar to CIN (convective \
            inhibition).</div>',

            'lfrh': '<div class="spc-prod">LCL-LFC Relative Humidity (%)</div><div class="spc-info">This is the mean relative humidity in the \
            layer between the LCL(<u><b>L</b></u>ifting <u><b>C</b></u>ondensation <u><b>L</b></u>evel)and the LFC (<u><b>L</b></u>evel of \
            <u><b>F</b></u>ree<u><b>C</b></u>onvection). Near saturation (RH=100%), from the LCL to the LFC, suggests that the LFC is near the \
            LCL.  When this occurs, a parcel experiencing forced ascent above the LCL may not be diluted with dry environmental air prior to \
            reaching the LFC. The height difference between the LCL and the LFC is important when determining convection initiation. The smaller \
            the difference between the LCL and the LFC, the more likely deep convection becomes. The LCL-LFC difference is similar to CIN \
            (convective inhibition).</div>',

            'skewt': '<div class="spc-prod">0-9 km AGL skew-T diagram </div><div class="spc-info">Display depicts the vertical profiles of \
            temperature (red) and dew point temperature (green), in the form of a standard skew-T/logP diagram for the lowest 9 km above ground \
            level. The 0 C and -20 C isotherms (dashed black and brown diagonal lines, respectively) are plotted for reference. The dashed \
            black curve denotes the "most unstable" lifted parcel trace (only when MUCAPE >= 100 J kg<sup>-1</sup>), and the shaded area \
            (light red) shows lifted parcel buoyancy.</div>',

            // Thermodynamics (Classic)

            'ttot': '<div class="spc-prod">Total Totals</div><div class="spc-info">The equation is:\
            <br><br>TT = (T850 - T500) + (Td850 - T500) ... or equivalently ... TT=T850 + Td850 - (2 x T500)</div>',

            'kidx': '<div class="spc-prod">K Index</div><div class="spc-info">The K index is a measure of thunderstorm potential based \
            on the vertical temperature lapse rate, and the amount and vertical extent of low-level moisture in the atmosphere.\
            <br><br>K = T(850 mb) + Td(850 mb) - T(500 mb) - DD(700 mb)<br><br>\
            in degrees C, where T represents temperature, Td represents dewpoint temperature, and DD represents dewpoint depression at the indicated level.\
            K < 30 --  Thunderstorms with heavy rain or severe weather possible (see note below).<br>\
            K > 30 --  Better potential for thunderstorms with heavy rain.<br>\
            K = 40 --  Best potential for thunderstorms with very heavy rain.<br><br>\
            In general, the higher the ambient or inflow K index value, the greater the potential for heavy rain. However, beware of low (less than 30) \
            values of K. Since the K index includes the dewpoint depression (i.e., difference between the temperature and dewpoint temperature) at 700 \
            mb, dry air at this level will cause a low K value. However, given moisture below 700 mb, unstable air, and a lifting mechanism, strong or \
            severe organized thunderstorms, and even heavy rain, can still occur. Scattered diurnal convection occurring in an environment containing \
            high K (and PW) values can cause a quick burst of very heavy rain.</div>',

            'show': '<div class="spc-prod">Showalter Index</div><div class="spc-info">The Showalter Index is a long-standing, simple stability \
            index uisng the 850 mb to 500 mb lifted index. </div><div class="spc-ref"><br>Additional Information \
            <a href="https://glossary.ametsoc.org/wiki/Stability_index" target="_blank">Here</a></div>',


            // Wind Shear

            'eshr': '<div class="spc-prod">Effective Bulk Wind Difference (kts)</div><div class="spc-info">The magnitude of the vector wind difference \
            from the effective inflow base upward to 50% of the equilibrium level height for the most unstable parcel in the lowest 300 mb. This parameter \
            is similar to the 0-6 km bulk wind difference, though it accounts for storm depth (effective inflow base to EL) and is designed to identify \
            both surface-based and "elevated" supercell environments. Supercells become more probable as the effective bulk wind difference increases \
            in magnitude through the range of 25-40 kt and greater.</div><div class="spc-ref"><br>Additional information \
            <a href="https://www.spc.noaa.gov/publications/thompson/effshear.pdf" target="blank">HERE</a></div>',

            'shr6': '<div class="spc-prod">SFC-6 km Vertical Shear Vector (kts)</div><div class="spc-info">The surface through 6-km above ground level shear vector \
            denotes the change in wind throughout this height.  Thunderstorms tend to become more organized and persistent as vertical shear increases. Supercells are \
            commonly associated with vertical shear values of 35-40 knots and greater through this depth.</div><div class="spc-ref">Additional information \
            <a href="https://www.spc.noaa.gov/publications/thompson/ruc-waf.pdf" target="_blank">here</a>.</div>',

            'shr8': '<div class="spc-prod">SFC-8 km Vertical Shear Vector (kts)</div><div class="spc-info">The surface through 8 km above ground level shear vector \
            denotes the change in wind throughout this height.  Thunderstorms tend to become more organized and persistent as vertical shear increases. Bunkers et al. \
            2006 found that long-lived supercells occur in environments with much stronger 0-8-km bulk wind shear ( > 50 kt) than that observed with short-lived supercells.\
            <div class="spc-ref">Reference: Bunkers, M.J., J.S. Johnson, L.J. Czepyha, J.M. Grzywacz, B.A. Klimowski and M.R. Hjelmfelt, 2006: An observational \
            examination of long-lived supercells. Part II: environmental conditions and forecasting. <i>Wea. Forecasting</i>, <b>21</b>, 689-714. </div>',

            'shr1': '<div class="spc-prod">SFC-1 km Vertical Shear Vector (kts)</div><div class="spc-info">Surface-1-km Vertical Shear is the difference \
            between the surface wind and the wind at 1-km above ground level. These data are plotted as vectors with shear magnitudes contoured.  0-1-km shear \
            magnitudes greater than 15-20 knots tend to favor supercell tornadoes.</div> \
            <div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc-waf.pdf" target="_blank">HERE</a>.</div>',

            'brns': '<div class="spc-prod">Bulk Richardson Number Shear (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">The BRN \
            (<u><b>B</b></u>ulk <u><b>R</b></u>ichardson <u><b>N</b></u>umber)shear is similar to the BL-6-km shear, except that the BRN Shear uses a \
            difference between the low-level wind and a density-weighted mean wind through the mid-levels.  Values of 35-40 m<sup>2</sup> s<sup>-2</sup> or \
            greater have been associated with supercells.</div>',

            'effh': '<div class="spc-prod">Effective Storm Relative Helicity (m <sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">Effective SRH \
            (<u><b>S</b></u>torm <u><b>R</b></u>elative <u><b>H</b></u>elicity) is based on threshold values of lifted parcel CAPE (100 J kg<sup>-1</sup>) and \
            CIN (-250 J kg<sup>-1</sup>). These parcel constraints are meant to confine the SRH layer calculation to the part of a sounding where lifted parcels \
            are buoyant, but not too strongly capped. For example, a supercell forms or moves over an area where the most unstable parcels are located a couple of \
            thousand feet above the ground, and stable air is located at ground level. The question then becomes "how much of the cool air can the supercell ingest \
            and still survive?" Our estimate is to start with the surface parcel level ... and work upward until a lifted parcels CAPE value increases to 100 \
            Jkg<sup>-1</sup> or more ... with an associated CIN greater than -250 Jkg<sup>-1</sup>. From the first level meeting the constraints (the "effective surface")\
            ... we continue to look upward in the sounding until a lifted parcel has a CAPE less than 100 Jkg<sup>-1</sup> OR a CIN less than -250 J kg<sup>-1</sup>. \
            Of the three SRH calculations displayed on the SPC mesoanalysis page, effective SRH is the most applicable across the widest range of storm environments, and \
            effective SRH discriminates as well as 0-1 km SRH between significant tornadic and nontornadic supercells.</div>\
            <div class="spc-ref">More information is available <b><a href="https://www.spc.noaa.gov/publications/thompson/eff-srh.pdf" target="_blank">here</div>',

            'srh5': '<div class="spc-prod">0-500 m Storm Relative Helicity (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">SRH (<u><b>S</b></u>torm \
            <u><b>R</b></u>elative<u><b>H</b></u>elicity) in the lowest 500 m AGL has been found by Coffer et al. (2019), October issue of <em>Weather and \
            Forecasting</em>, to be a better discriminator than effective SRH between significant tornadoes and nontornadic supercells.  This calculation \
            of 0-500 m SRH is limited to within the effective inflow layer ... as long as the inflow base is at the ground.</div>',

            'srh1': '<div class="spc-prod">Storm Relative Helicity (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">SRH (<u><b>S</b></u>torm <u><b>R</b></u>elative<u><b>H</b></u>elicity) \
            is a measure of the potential for cyclonic updraft rotation in right-moving supercells, and is calculated for the lowest 1-km and 3-km layers above ground level. \
            There is no clear threshold value for SRH when forecasting supercells, since the formation of supercells appears to be related more strongly to the deeper \
            layer vertical shear.  Larger values of 0-3-km SRH (greater than 250 m<sup>2</sup> s<sup>-2</sup>) and 0-1-km SRH (greater than 100 m<sup>2</sup> s<sup>-2</sup>), \
            however, do suggest an increased threat of tornadoes with supercells. For SRH, larger values are generally better, but there are no clear thresholds between \
            non-tornadic and significant tornadic supercells.</div><div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" taget="_blank">HERE</a>.</div>',

            'llsr': '<div class="spc-prod">Surface-2-km Storm Relative Winds (kts)</div><div class="spc-info">Low-Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) \
            winds (0-2-km) are meant to represent low-level storm inflow. The majority of sustained supercells have 0-2-km storm inflow values of 15-20 knots or greater.</div>',

            'mlsr': '<div class="spc-prod">4-6-km Storm Relative Winds (kts)</div><div class="spc-info">Mid-Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) winds \
            (4-6-km) are of some use in discriminating between tornadic and non-tornadic supercells.  Tornadic supercells tend to have 4-6-km SR wind speeds in excess \
            of 15 knots, while non-tornadic supercells tend to have weaker mid-level storm-relative winds.</div><div class="spc-ref">\
            Reference: Thompson, R. L., 1998:  Eta model storm-relative winds associated with tornadic and nontornadic supercells.  <i>Wea. Forecasting,</i>, <b>13</b>, 125-137.</div>',

            'ulsr': '<div class="spc-prod">Anvil Level/9-11-km SR Winds (kts)</div><div class="spc-info">The Anvil Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) winds and \
            SR winds from 9-11-km are meant to discriminate supercell type.  In general, upper-level SR winds less than 40 knots correspond to "high precipitation" supercells, \
            40-60 knots SR winds denote "classic" supercells, while SR winds greater than 60 knots correspond to "low precipitation" supercells.</div><div class="spc-ref">\
            Reference: Rasmussen, E. N., and J. M. Straka, 1998: Variations in supercell morphology.  Part I:  Observations of the role of upper-level storm-relative flow. \
            <em>Mon. Wea. Rev.</em>, <b>126</b>, 2406-2421.</div>',

            'mnwd': '<div class="spc-prod">850-300 mb Mean Wind</div><div class="spc-info"> (kts; solid blue > 30 kts). Steering flow. Storms moving to right of \
            mean wind may ingest better streamwise horizontal vorticity/SRH.</div>',

            'xover': '<div class="spc-prod">850mb and 500mb Wind Crossover</div><div class="spc-info">Determines the presences of deep layer directional shear, which is often \
            favorable for supercells</div>',

            'srh3_chg': '<div class="spc-prod">3hr 0-3km SRH (m<sup>2</sup> s<sup>-2</sup>) and current storm motion estimate (kt)</div><div class="spc-info">3 hour change in SRH</div>',

            'srh1_chg': '<div class="spc-prod">3hr 0-1km SRH (m<sup>2</sup> s<sup>-2</sup>) and current storm motion estimate (kt)</div><div class="spc-info">3 hour change in SRH</div>',

            'shr6_chg': '<div class="spc-prod">3hr 0-6km Bulk Shear (barbs - kt) and change (kt)</div><div class="spc-info">3 hour change in 0-6km Bulk Shear</div>',

            'hodo': '<div class="spc-prod">0-9 km AGL hodograph</div><div class="spc-info">Display depicts ground-relative hodographs from the 1-h RAP model forecast and latest \
            merged surface analysis [the hodograph connects the ends of the individual wind vectors, plotted from the origin (the small crosshair)]. \
            Color coding is as follows:  0-500 m (magenta), 500-3000 m (red), 3000-6000 m (green), and 6000-9000 m (yellow).  The dashed gray range rings \
            denote wind speeds of 20 and 40 kt. Hodographs are only plotted where MUCAPE >= 100 J kg<sup>-1</sup>. The red and blue circles represent Bunkers \
            right and left storm motion, respectively. The area within the effective inflow layer is shaded blue. The brown squares denote Bunkers mean wind \
            (pressure weighted) in the lowest 65% of storm depth (effective inflow base to 65% of MU parcel equilibrium level height). In cases where the LFC \
            is above the effective inflow layer, an orange dashed line is plotted.</div>',

            // Composite Indices

            'scp': '<div class="spc-prod">Supercell Composite Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes \
            effective storm-relative helicity (ESRH, based on Bunkers right supercell motion), most unstable parcel CAPE (muCAPE) and convective inhibition \
            (muCIN), and effective bulk wind difference (EBWD). Each ingredient is normalized to supercell "threshold" values, and larger values of SCP denote greater \
            "overlap" in the three supercell ingredients. Only positive values of SCP are displayed, which correspond to environments favoring right-moving (cyclonic) \
            supercells. This index is formulated as follows:<br>SCP = (muCAPE / 1000 J kg<sup>-1</sup>) * (ESRH / 50 m<sup>2</sup> s<sup>-2</sup>) * \
            (EBWD / 20 m s<sup>-1</sup>) * (-40 J kg<sup>-1</sup> / muCIN)<br><br>EBWD is divided by 20 m s<sup>-1</sup> in the range of 10-20 m s<sup>-1</sup>. EBWD \
            less than 10 m s<sup>-1</sup>is set to zero, and EBWD greater than 20 m s<sup>-1</sup> is set to one. The muCIN term is based on work by Gropp and Davenport \
            (2018), August issue of <em>Weather and Forecasting</em>, and it is set to 1.0 when muCIN is greater than -40 kg<sup>-1</sup>.</div><div class="spc-ref">Additional \
            information can be found <a href="https://www.spc.noaa.gov/publications/thompson/stp_scp.pdf" target_"blank">here</a>.</div>',

            'stor': '<div class="spc-prod">Significant Tornado Parameter (fixed layer)</div><div class="spc-info">A multiple ingredient, composite index that \
            includes 0-6 km bulk wind difference (6BWD), 0-1 km storm-relative helicity (SRH1), surface parcel CAPE (sbCAPE), and surface parcel LCL \
            height (sbLCL). This version of STP mimics the formulation presented by Thompson et al. (2012) by using fixed-layer calculations of vertical \
            shear, and substitutes the surface lifted parcels as an alternative to the ML parcels in the "effective layer" version of STP. \
            The index is formulated as follows:<br><br> STP = (sbCAPE/1500 J kg<sup>-1</sup>) * ((2000-sbLCL)/1000 m) * (SRH1/150 m<sup>2</sup> s<sup>-2</sup>) * \
            (6BWD/20 m s<sup>-1</sup>)* ((200+sbCIN)/150 J kg<sup>-1</sup>) <br><br>The sbLCL term is set to 1.0 when sbLCL < 1000 m, and set to 0.0 when sbLCL > 2000 m; \
            the sbCIN term is set to 1.0 when sbCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when sbCIN < -200; the 6BWD term is capped at a value of 1.5 for 6BWD > \
            30 m s<sup>-1</sup>, and set to 0.0 when 6BWD < 12.5 m s<sup>-1</sup>.<br><br> A majority of significant tornadoes (F2 or greater damage) have been \
            associated with STP values greater than 1, while most non-tornadic supercells have been associated with values less than 1 in a large sample of RAP \
            analysis proximity soundings.</div><div class="spc-ref">Additional information can be found <a href="https://www.spc.noaa.gov/publications/thompson/waf-env.pdf" target="_blank">here</a></div>',

            'stpc': '<div class="spc-prod">Significant Tornado Parameter (effective layer)</div><div class="spc-info">A multiple ingredient, composite index that \
            includes effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean parcel \
            CIN (mlCIN), and 100-mb mean parcel LCL height (mlLCL). The index is formulated as follows:<br><br> \
            STP = (mlCAPE/1500 J kg<sup>-1</sup>) * ((2000-mlLCL)/1000 m) * (ESRH/150 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * \
            ((200+mlCIN)/150 J kg<sup>-1</sup>)<br><br>The mlLCL term is set to 1.0 when mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; the mlCIN term \
            is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > 30 m s<sup>-1</sup>, \
            and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>.  Lastly, the entire index is set to 0.0 when the effective inflow base is above the ground. A majority of \
            significant tornadoes (F2 or greater damage) have been associated with STP values greater than 1 within an hour of tornado occurrence, while most non-tornadic \
            supercells have been associated with values less than 1 in a large sample of RAP analysis proximity soundings.<div class="spc-ref">Additional information \
            can be found <a href="https://www.spc.noaa.gov/publications/thompson/waf-env.pdf" target="_blank">here</a>.</div>',

            'stpc5': '<div class="spc-prod">Significant Tornado Parameter (uses 0-500 m SRH within effective inflow layer)</div><div class="spc-info">A multiple ingredient, \
            composite index that includes effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean \
            parcel CIN (mlCIN), and 100-mb mean parcel LCL height (mlLCL). The index is formulated as follows:<br><br> STP = (mlCAPE/1500 J kg<sup>-1</sup>) * \
            ((2000-mlLCL)/1000 m) * (0-500 m SRH/75 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * ((200+mlCIN)/150 J kg<sup>-1</sup>)<br><br> The 0-500 m SRH \
            is limited to within the effective inflow layer, if it exists.  The mlLCL term is set to 1.0 when mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; \
            the mlCIN term is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > \
            30 m s<sup>-1</sup>, and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>.  Lastly, the entire index is set to 0.0 when the effective inflow base is above \
            the ground. A majority of significant tornadoes (F2 or greater damage) have been associated with STP values greater than 1 within an hour of tornado \
            occurrence, while most non-tornadic supercells have been associated with values less than 1 in a large sample of RAP analysis proximity soundings.  \
            Replacing effective SRH with 0-500 m SRH improves discrimination between significant tornadoes and non-tornadic supercells, per work by Coffer et al. (2019), \
            October issue of <em>Weather and Forecasting</em>.</div><div class="spc-ref">Additional information can be \
            found <a href="https://journals.ametsoc.org/view/journals/wefo/34/5/waf-d-19-0115_1.xml" target="_blank">here</a>.</div>',

            'sigt1': '<div class="spc-prod">Conditional Probability of a Significant Tornado (Eqn 1)</div><div class="spc-info">Contour analysis of conditional significant \
            (EF2+) tornado probabilities that are estimated via two forms of a linear regression equation.  The probability is conditional on the occurrence of a supercell \
            thunderstorm. The components of the significant tornado parameter (STP) make up the basis of the two regression equations, both of which use a product of the \
            0-6 km bulk wind difference and the square root of MLCAPE,and MLCIN. The primary variation between the two conditional probability equations involves the use \
            of 0-1 km SRH (equation 1) and the 0-1 km bulk wind difference (equation 2).  The conditional probabilities tend to overestimate the rate of occurrence of \
            signficant tornadoes,especially where the initial convective mode is nondiscrete, or where the mode evolves from discrete to linear. The regression equations \
            complement the STP in a probabilistic sense, and overall performance is similar to the STP.</div><div class="spc-ref">Additional information <br>\
            Togstad, W. E., J. M. Davies, S. J. Corfidi, D.R. Bright, and A. R. Dean, 2011:  Conditional probability estimation for significant tornadoes based on \
            Rapid Update Cycle (RUC) profiles.  Wea. Forecasting, 26, 729-743.</div>',

            'sigt2': '<div class="spc-prod">Conditional Probability of a Significant Tornado (Eqn 2)</div><div class="spc-info">Contour analysis of conditional significant \
            (EF2+) tornado probabilities that are estimated via two forms of a linear regression equation.  The probability is conditional on the occurrence of a supercell \
            thunderstorm. The components of the significant tornado parameter (STP) make up the basis of the two regression equations, both of which use a product of the \
            0-6 km bulk wind difference and the square root of MLCAPE,and MLCIN. The primary variation between the two conditional probability equations involves the use \
            of 0-1 km SRH (equation 1) and the 0-1 km bulk wind difference (equation 2).  The conditional probabilities tend to overestimate the rate of occurrence of \
            signficant tornadoes,especially where the initial convective mode is nondiscrete, or where the mode evolves from discrete to linear. The regression equations \
            complement the STP in a probabilistic sense, and overall performance is similar to the STP.</div><div class="spc-ref">Additional information <br>\
            Togstad, W. E., J. M. Davies, S. J. Corfidi, D.R. Bright, and A. R. Dean, 2011:  Conditional probability estimation for significant tornadoes based on \
            Rapid Update Cycle (RUC) profiles.  Wea. Forecasting, 26, 729-743.</div>',

            'nstp': '<div class="spc-prod">Non-Supercell Tornado parameter (NST)</div><div class="spc-info">The non-supercell tornado parameter (NST) is the normalized \
            product of the following terms:<br><br>(0-1 km lapse rate/9 C/km) * (0-3 km MLCAPE/100 J/kg) * ((225 - MLCIN/200) * ((18 - 0-6 km bulk wind \
            difference)/5 m/s) * (surface relative vorticity/8**10-5/s)<br><br>This normalized parameter is meant to highlight areas where steep \
            low-level lapse rates correspond with low-level instability, little convective inhibition, weak deep-layer vertical shear, and large \
            cyclonic surface vorticity.  Values > 1 suggest an enhanced potential for non-mesocyclone tornadoes.</div><div class="spc-ref">Additional Information \
            <a href="http://ams.confex.com/ams/23SLS/techprogram/paper_115294.htm" target="_blank">HERE</a></div>',

            'vtp3': '<div class="spc-prod">Violent Tornado Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes \
            effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean parcel CIN (mlCIN), \
            and 100-mb mean parcel LCL height (mlLCL), 0-3 km mean parcel CAPE and 0-3 km lapse rates. The index is formulated as follows:<br><br> \
            VTP = (mlCAPE/1500 J kg<sup>-1</sup>) * ((2000-mlLCL)/1000 m) * (ESRH/150 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * \
            ((200+mlCIN)/150 J kg<sup>-1</sup>) * (0-3 km MLCAPE/50 J kg<sup>-1</sup>) * (0-3 km Lapse Rate/6.5 &#8451 km<sup>-1</sup>)<br><br>The \
            0-3 km lapse rate term is set to 2.0 when 0-3 km MLCAPE > 100 J kg<sup>-1</sup>.  Like STP, the mlLCL term is set to 1.0 when \
            mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; the mlCIN term is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when \
            mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > 30 m s<sup>-1</sup>, and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>. \
            Lastly, the entire index is set to 0.0 when the effective inflow base is above the ground. Research using observed soundings found that 0-3 km \
            CAPE and 0-3 km lapse rate were notable discriminators of violent tornado environments (verses weak and/or significant tornado environments). \
            These parameters were combined into the effective layer version of the Significant Tornado Parameter (STP) to create the Violent Tornado Parameter \
            (VTP).</div><div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/mosier/2018-JOM1.pdf" target="_blank">HERE</a>.</div>',

            'sigh': '<div class="spc-prod">Significant Hail Parameter</div><div class="spc-info">Visit <a href="https://www.spc.noaa.gov/exper/mesoanalysis/help/help_sigh.html"\
            target="_blank">https://www.spc.noaa.gov/exper/mesoanalysis/help/help_sigh.html</a> for details.</div>',

            'sars1': '<div class="spc-prod">SARS Hail Size</div><div class="spc-info">The SARS method returns a maximum expected hail report by matching existing environmental \
            conditions to historic severe hail cases. These forecast maximum sizes are conditional on severe hail of any size occurring.<br><br>This graphic shows the \
            "best guess" maximum hail report.</div> ',

            'sars2': '<div class="spc-prod">SARS Significant Hail Percentage and Conditional Matches</div><div class="spc-info">The SARS method returns a maximum \
            expected hail report by matching existing environmental conditions to historic severe hail cases. These forecast maximum sizes are conditional on \
            severe hail of any size occurring. This graphic shows two items: First, the color fill denotes the percent of matching analog soundings that \
            had significant (2" diameter or larger) hail. Color fill starts at 50 percent. Second, the contours denote the actual number of matching cases \
            for each grid point. Percentiles for the number of matches are based on a set of about 1200 severe hail cases. For example, a grid point that has over \
            100 matches suggests a "common" severe hail environment, while a grid point with 5 matches would suggest severe hail is unlikely. A high number of matches, \
            combined with a high significant hail percentage would suggest significant hail is likely.</div>',

            'lghl': '<div class="spc-prod">Large Hail Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes three thermodynamic \
            components [MUCAPE, 700-500 mb lapse rates, the depth of the hail growth zone (-10 to -30 C)], as well as three vertical shear components \
            [surface to EL bulk shear, the direction difference between the ground-relative winds at the EL and in the 3-6 km layer, and the direction difference \
            between the storm-relative winds in the 3-6 km and 0-1 km layers]. The index is formulated as follows:<br><br>If if 0-6 km BWD < 14 m s <sup>-1</sup> \
            or MUCAPE < 400 J kg<sup>-1</sup>, LHP = 0.  If both the shear and MUCAPE are >= to the above conditions (a loose supercell check): <br> LHP = (TERM A * TERM B) + \
            5 <br> TERM A = (((MUCAPE-2000)/1000) + ((3200-THK<sub>HGZ</sub>)/500) + ((LR<sub>75</sub>-6.5)/2)) where THK<sub>HGZ</sub> is the depth of the hail growth zone \
            (the -10 to -30 C layer), and LR<sub>75</sub> is the 700-500 mb temperature lapse rate. <br> TERM B = (((Shear<sub>EL</sub>-25)/5) + ((GRW<sub>dirEL</sub>+5)/20) + \
            ((SRW<sub>dirMID</sub>-80)/10)) where Shear<sub>EL</sub> is the magnitude of the vector wind difference between the surface wind and the mean wind in the 1.5 km \
            layer immediately below the EL height for the MU parcel, GRW<sub>dirEL</sub> is the directional difference between the ground-relative mean wind in the 1.5 km \
            layer below the EL and the mean wind in the 3-6 km layer AGL, and SRW<sub>dirMID</sub> is the directional difference betweem the mean storm-relative winds in the 3-6 km \
            and 0-1 km layers. <br> The LHP is meant to discriminate between significant hail (>= 2 inch diameter and smaller hail). </div><div class="spc-ref"> \
            Additional information <a href="http://www.ejssm.org/ojs/index.php/ejssm/article/view/137/101" target="_blank">HERE</a>.</div>',

            'dcp': '<div class="spc-prod">Derecho Composite Parameter (DCP)</div><div class="spc-info">This parameter is based on a data set of 113 derecho events compiled by \
            Evans and Doswell (2001).  The DCP was developed to identify environments considered favorable for cold pool "driven" wind events through four primary mechanisms: <br>\
            1) Cold pool production [DCAPE]<br>2) Ability to sustain strong storms along the leading edge of a gust front [MUCAPE]<br>3) Organization potential for any ensuing \
            convection [0-6 km shear]<br>4) Sufficient flow within the ambient environment to favor development along downstream portion of the gust front [0-6 km mean wind]. \
            This index is fomulated as follows: <br> DCP = (DCAPE/980)*(MUCAPE/2000)*(0-6 km shear/20 kt)*(0-6 km mean wind/16 kt)</div><div class="spc-ref">Reference: <br>\
            Evans, J.S., and C.A. Doswell, 2001: Examination of derecho environments using proximity soundings.  <i>Wea. Forecasting</i>, <b>16</b>, 329-342.</div>',

            'cbsig': '<div class="spc-prod">Craven SigSvr Parameter</div><div class="spc-info">The simple product of 100mb MLCAPE and 0-6km magnitude of the vector difference \
            (m/s; often referred to as "deep layer shear") accounts for the compensation between instability and shear magnitude.  Using a database of about 60,000 soundings, \
            the majority of significant severe events (2+ inch hail, 65+ knot winds, F2+ tornadoes) occur when the product exceeds 20,000 m3/s3. The index is formulated as \
            follows:<br>C = (MLCAPE J kg<sup>-1</sup>) * (SHR6 m s<sup>-1</sup>)<br>For example, a 0-6-km shear of 20 m s<sup>-1</sup> (40 knots) and CAPE of \
            3000 J kg<sup>-1</sup> results in a Craven SigSvr index of 60,000.  Units are scaled to the nearest 1000 on the web plot.</div><div class="spc-ref">Reference: <br>\
            Craven, J. P., and H. E. Brooks, 2004:  Baseline climatology of sounding derived parameters associated with deeep moist convection.  <em> Natl. Wea. Digest</em>, <b>28</b>, 13-24.</div>',

            'brn': '<div class="spc-prod">Bulk Richardson Number</div><div class="spc-info">The bulk Richardson number (BRN) is a ratio of buoyancy to vertical shear: \
            BRN = (MLCAPE) / 0.5 * (U)**2 where U = the wind speed difference between the density weighted 0-6 km mean wind and the lowest 500 m mean wind. The BRN is meant to \
            estimate the balance between vertical shear and buoyancy, with low BRN values suggestive of vertical shear that is too strong relative to the buoyancy, and large BRN \
            values are suggestive of multicell clusters. Intermediate BRN values favor sustained supercells. BRN values in the range of 10-45 (dimesionless) have been associated \
            with supercells via numerical simulations.  Close proximity soundings reveal supercell environments with larger CAPE and larger resultant BRN values (in the range of \
            50-100) than suggested by the original modeling work of Weisman and Klemp (1982).</div><div class="spc-ref">References:<br> Weisman, M. L., and J. B. Klemp, 1982: \
            The dependence of numerically simulated convective storms on vertical wind shear and buoyancy.  Mon. Wea. Rev., 110, 504-520. <br>Thompson, R. L., R. Edwards, \
            J. A. Hart, K. L. Elmore, and P. Markowski, 2003:  Close proximity soundings within supercell environments obtained from the Rapid Updage Cycle.  Wea. Forecasting, \
            18, 1243-1261.<br>Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" target="_blank">HERE</a>.</div>',

            'mcsm': '<div class="spc-prod">Probability of MCS maintenance</div><div class="spc-info">348 warm-season MCS proximity soundings from a variety of MCS types were \
            used to develop this parameter.  Though hypothesis testing and discriminant analysis on hundreds of sounding parameters, the following four parameters were selected \
            to develop the probabilities: <br>1) maximum bulk shear (m/s) in the 0-1 and 6-10 km layer<br>2) 3-8 km lapse rate (degrees C/km)<br>3) most unstable CAPE<br>4) \
            3-12 km mean wind speed (m/s)</div><div class="spc-ref">Reference: <br> Coniglio, M.C., and S.F. Corfidi, 2006: Forecasting the speed and longevity of <br>\
            severe mesoscale convective systems. Preprints, Severe Local Storms Symposium, Amer. Meteor. Soc., Atlanta, GA, CD-ROM.</div>',

            'mbcp': '<div class="spc-prod">Microburst Composite</div><div class="spc-info">The Microburst Composite is a weighted sum of the following individual parameters: \
            SBCAPE, SBLI, lapse rates, vertical totals (850-500 mb temperature difference), DCAPE, and precipitable water. The specific terms and weights are listed below: <br>\
            SBCAPE term -> < 3100 set to 0; 3100-3999 set to 1; >= 4000 set to 2; \
            SBLI term -> > -8 set to 0; <= -8 set to 1; <= -9 set to 2; <= -10 set to 3; \
            0-3 km lapse rate term -> <= 8.4 set to 0; > 8.4 set to 1; vertical totals term -> < 27 set to \
            0; >= 27 set to 1; >= 28 set to 2; >= 29 set to 3; DCAPE term -> < 900 set to 0; >= 900 set to 1; >= 1100 set to 2; >= 1300 set to 3; \
            precipitable water term -> <= 1.5 set to -5; > 1.5 set to 0.<br>\
            All six of the terms are summed to arrive at the final microburst composite value.<br>\
            3-4 = "slight chance" of a microburst<br>\
            5-8 infers a "chance" of a microburst<br>\
            >= 9 infers that microbursts are "likely".<br>These values are conditional upon the existence of a storm. </div>',

            'desp': '<div class="spc-prod">Enhanced Stretching Potential</div><div class="spc-info">This non-dimensional composite parameter based on work by Jon Davies that identifies \
            areas where low-level buoyancy and steep low-level lapse rates are co-located, which may favor low-level vortex stretching and tornado potential.  ESP is formulated as \
            follows: <br><br> ESP = (0-3 km MLCAPE / 50 J kg<sup>-1</sup>) * ((0-3 km lapse rate - 7.0) / 1.0 C km<sup>-1</sup>) <br><br> where ESP is set to zero when the 0-3 km lapse rate \
            is < 7 C km<sup>-1</sup>, or when total MLCAPE < 250 J kg<sup>-1</sup>.</div><div class="spc-ref">Additional information <a href="http://nwafiles.nwas.org/ej/pdf/2005-EJ4.pdf" \
            target="_blank">HERE</a>.</div>',

            'ehi1': '<div class="spc-prod">Energy-Helicity Index (Sfc-1 km)</div><div class="spc-info">The basic premise behind the EHI (<u><b>E</b></u>nergy-<u><b>H</b></u>elicity \
            <u><b>I</b></u>ndex) is that storm rotation should be maximized when CAPE is large and SRH is large.  0-1-km EHI values greater than 1-2 have been associated with \
            significant tornadoes in supercells.</div><div class="spc-ref">References:<br> Rasmussen, E. N., 2003: Refined supercell and tornado forecast parameters. \
            <i>Wea. Forecasting,</i>, <b>18</b>, 530-535. <br><br> Thompson, R. L., R. Edwards, J. A. Hart, K. L. Elmore, and P. Markowski, 2003:  Close proximity soundings \
            within supercell environments obtained from the Rapid Updage Cycle.  <i>Wea. Forecasting,</i> <b>18</b>, 1243-1261.<br>Additional information \
            <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" target="_blank">HERE</a></div>',

            'ehi3': '<div class="spc-prod">EHI3</div>Energy-Helicity Index (Sfc - 3km)</div><div class="spc-info">The basic premise behind the EHI \
            (<u><b>E</b></u>nergy-<u><b>H</b></u>elicity <u><b>I</b></u>ndex) is that storm rotation should be maximized when CAPE is large and SRH is large. \
            0-3-km EHI values greater than 1-2 have been associated with significant tornadoes in supercells.</div>',

            'vgp3': '<div class="spc-prod">Vorticity Generation Parameter (m s<sup>-2</sup>)</div><div class="spc-info">The VGP (<u><b>V</b></u>orticity <u><b>G</b></u>eneration \
            <u><b>P</b></u>arameter) is meant to estimate the rate of tilting and stretching of horizontal vorticity by a thunderstorm updraft.  Values greater than \
            0.2 m s<sup>-2</sup> suggest an increasing possibility of tornadic storms.</div><div class="spc-ref"> \
            Reference:<br> Rasmussen, E. N., and D. O. Blanchard, 1998: A baseline climatology of sounding-derived supercell and tornado forecast parameters. \
            <em>Wea. Forecasting.</em>, <b>13</b>, 1148-1164.</div>',

            'crit': '<div class="spc-prod">Critical Angle</div><div class="spc-info">The "critical angle" is the angle between the storm-relative wind at the surface and the 0-500 m \
            AGL shear vector [(kt) displayed only for areas where the effective inflow base is the ground (SBCAPE 100 J kg<sup>-1</sup> or greater, and less than 250 J kg<sup>-1</sup> \
            CIN]. A critical angle near 90 degrees infers streamwise vorticity near the ground, which favors stronger cyclonic rotation and dynamically forced ascent closer to the ground in a \
            right-moving supercell (through the effects of tilting and stretching of horizontal vorticity).  Critical angles in the range of 45 to 135 degrees suggest near-surface \
            vorticity is more streamwise than crosswise, and values in this range are highlighted by the color fill.  Large SRH colocated with a critical angle close to 90 degrees is \
            most favorable for tornadic supercells.</div><div class="spc-ref">Additional information \
            <a href="http://www.ejssm.org/ojs/index.php/ejssm/article/view/33/38" target="_blank">HERE</a>.</div>',


            // Multi-parameter (Beta)

            'sherbe': '<div class="spc-prod">SHERBE></div><div class="spc-info">The SHERBE is a normalized composite parameter intended to identify the potential for significant \
            damaging winds and tornadoes in low CAPE, high shear environments typical of the southeast U.S. cool season.\
            <br><br>SHERBE = (LR<sub>0-3</sub>/5.2) * (LR<sub>75</sub>/5.6) * (EBWD/27)<br><br> \
            where the lapse rate (LR) terms apply to the 0-3 km and 700-500 mb layers (C km<sup>-1</sup>), respectively, and the EBWD is the effective bulk wind \
            difference (m s<sup>-1</sup>). This formulation of SHERBE inherently accounts for at least weak buoyancy by utilizing the EBWD (which requires an effective \
            inflow layer), which tends to reduce false alarms compared to the original version of SHERB using the fixed-layer 0-3 km shear.  Still, the parameter can \
            suggest an over-estimate of the severe weather threat in areas of relatively steep 0-3 km lapse rates which overlap with the 700-500 mb layer in the vertical. \
            </div><div class="spc-ref"><br>Additional information <a href="http://journals.ametsoc.org/doi/pdf/10.1175/WAF-D-13-00041.1" target="_blank">here</a>.</div>',

            'moshe': '<div class="spc-prod">Modified SHERBE</div><div class="spc-info">The Modified SHERBE is a composite parameter designed to highlight "low CAPE/high shear" \
            environments capable of producing significant severe storms.  MOSHE is formulated as follows:\
            <br><br>MOSHE = ((0-3 km lapse rate - 4 K km<sup>-1</sup>)<sup>2</sup> / 4 K<sup>2</sup> km<sup>-2</sup>) * ((0-1.5 km bulk shear - 8.0 m s<sup>-1</sup>) / \
            10 m s<sup>-1</sup>) * ((effective bulk shear - 8 m s<sup>-1</sup>) / 10 m s<sup>-1</sup>) * (MAXTEVV + 10 K Pa km <sup>-1</sup> s<sup>-1</sup>) / 9 K Pa km<sup>-1</sup> \
            s<sup>-1</sup>)<br><br>\
            where MAXTEVV is the maximum product of theta-e decrease with height and upward motion at the top of each 2 km deep layer from the surface to 6 km, incremented every \
            0.5 km. This composite parameter indirectly includes some influence of buoyancy through the effective bulk shear term, which requires at least 100 J kg<sup>-1</sup> of \
            CAPE and no more than 250 J kg<sup>-1</sup> of CIN.  Overall, MOSHE represents and improvement to the original SHERB parameters developed by Sherburn et al. (2014), \
            primarily through reduction in false alarm area.  Please note that this parameter formulation is very sensitive to the magnitude of vertical velocity, and may not \
            translate well between differing modeling systems (e.g., the RAP model versus a convection-allowing model).</div><div class="spc-ref"><br>\
            Additional information can be found <a href="http://journals.ametsoc.org/doi/pdf/10.1175/WAF-D-16-0086.1" target="_blank">here</a>.</div>',

            'cwasp': '<div class="spc-prod">Craven-Wiedenfeld Aggregate Severe Parameter</div><div class="spc-info">This aggregate parameter is the sum of 33 individual weighted \
            parameters, ranging from mandatory pressure level winds, temperature and moisture, to CAPE and vertical shear. Typical ranges of values were established for \
            each parameter in association with significant tornado (EF2+) events, and a numerical weight of 0-3 was assigned to each parameter. If all parameters are \
            consistent with historical EF2+ tornado events, the CWASP total will reach a maximum value of 99.  The majority of EF2+ tornadoes have occurred with CWASP values \
            above about 70.</div><div class="spc-ref"><br>Additional information \
            <a href="//www.nws.noaa.gov/cgi-bin/nwsexit.pl?url=//ftp.nwas.org/meetings/nwa2012/extendedabstracts/NWA2012_D8.2_Craven_Wiedenfeld.pdf" target="_blank">here</a>.</div>',

            'tts': '<div class="spc-prod">Tornadic Tilting and Stretching parameter (TTS)</div><div class="spc-info">TTS is a parameter developed by Jon Davies that \
            focuses on storm-relative helicity in the lowest 1 km (SRH1) and 100 mb mixed-layer CAPE in the lowest 3 km above ground level (mlCAPE3). The presence of \
            both ingredients suggests potential for increased low-level tilting and stretching of horizontal, streamwise vorticity within updrafts, which may increase the \
            potential for tornadic supercells. Enhancements are added based on total CAPE and deep-layer shear that strengthen updrafts; LCL height and CIN are used as \
            limiting factors when they are too high or large, respectively. In preliminary testing, values approaching 2 and greater suggest potential for tornadic \
            supercells. This experimental parameter is intended to help diagnose environments supporting tornadoes where total CAPE is relatively small, such as during \
            the cool season. This non-dimensional parameter is formulated as follows:<br><br>\
            TTS = ((SRH1 * mlCAPE3)/6500) * ((mlCAPE/2000 J kg -1)) * (6BWD/20 m s-1)<br><br>\
            In the first term, mlCAPE3 is capped at 150 J kg-1; the mlCAPE term is set to 1.0 if total mlCAPE < 2000 J kg-1 and is capped at 1.5 for mlCAPE > 3000 J \
            kg -1; the 6BWD term is capped at 1.5 for 6BWD > 30 m s-1 and set to zero when 6BWD < 12.5 m s-1 (similar to STP); if mlLCL > 1700 m AGL, or mlCIN < -100 J kg-1, \
            or sbCIN < -200 J kg-1, or TTS < 0, TTS is set to zero.</div>',

            'tehi': '<div class="spc-prod">Tornadic 0-1 km EHI</div><div class="spc-info">This updated version of the 0-1 km EHI adds 0-3 km mlCAPE and 0-6 km bulk wind difference as \
            enhancing factors, and LCL/CIN as limiting factors. Because EHI values are often deceptively large over wide areas when other factors suggest reduced \
            potential for tornadic supercells (such as weak 0-6 km bulk wind difference, high LCL heights, or large nighttime CIN), this modified version of EHI \
            should consolidate areas supporting tornadic supercells (values of 1-2 or greater). The inclusion of 0-3 km mlCAPE also helps identify areas with greater \
            potential for low-level stretching, even if total mlCAPE is relatively small. This non-dimensional parameter (updated by Jon Davies) is formulated as follows:\
            <br><br>TEHI = ((SRH1 * mlCAPE)/160,000) * ((mlCAPE3/200 J kg -1)) * (6BWD/20 m s-1)<br><br>\
            The mlCAPE3 term is set to 1.0 if total mlCAPE > 1500 J kg-1, and is capped at 1.5 for mlCAPE3 > 300 J kg -1; the 6BWD term is capped at 1.5 for 6BWD > \
            30 m s-1 and set to zero when 6BWD < 12.5 m s-1 (similar to STP); if mlLCL > 1700 m AGL, or mlCIN < -100 J kg-1, or sbCIN < -200 J kg-1, or TEHI < 0, TEHI is set to zero.</div>',

            'ptstpe': '<div class="spc-prod">Conditional probability of EF0+ tornadoes</div><div class="spc-info">The conditional probability of EF0+ tornadoes \
            given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
            2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
            values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
            climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
            climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
            <a href="https://www.spc.noaa.gov/publications/smith/fig8_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. <br>\
            </div><div class="spc-ref">see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> for additional details.</div>',

            'pstpe': '<div class="spc-prod">Conditional probability of EF2+ tornadoes</div><div class="spc-info">The conditional probability of EF2+ tornadoes \
            given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
            2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
            values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
            climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
            climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
            <a href="https://www.spc.noaa.gov/publications/smith/fig8_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. \
            </div><div class="spc-ref">Please see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> \
            for additional details.</div>',

            'pvstpe': '<div class="spc-prod">Conditional probability of EF4+ tornadoes</div><div class="spc-info">The conditional probability of EF4+ tornadoes \
            given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
            2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
            values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
            climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
            climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
            <a href="https://www.spc.noaa.gov/publications/smith/fig8_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. Please \
            see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> for additional details.</div>',


            // Multi-Parameter Fields

            'lclsrh': '100 mb Mean LCL Height (dashed green &lt; 1250 m, solid orange > 1500 m, shaded > 1750 m) and 0-1 km SRH (solid blue > 50 m2/s2). Dashed green LCLs more favorable for tornadoes.',

            'lr3c': '<div class="spc-prod">0-3 km Lapse Rate (> 7 deg C/km shaded) and 0-3 km MLCAPE (solid red).</div><div class="spc-info">Very useful for determining where \
            mesovortexgenesis could be particularly robust if low-level MLCAPE is available to enhance stretching</div>',

            '3cvr': '<div class="spc-prod">3-km CAPE (J/kg) & Surface Vorticity</div><div class="spc-info">CAPE in the lowest 3-km above ground level, and surface relative vorticity. \
            Areas of large 0-3-km CAPE tend to favor strong low-level stretching, and can support tornado formation when co-located with significant vertical vorticity \
            near the ground.</div>',

            'tdlr': 'Surface Dewpoint (solid light green > 48 F, dark green > 60 F) and 700-500 mb Lapse Rate (solid red > 7 C/km).',

            'hail': '<div class="spc-prod">Hail Forecasting Parameters</div><div class="spc-info">This image depicts three forecasting parameters used to predict hail. They are CAPE in the \
            layer from -10 C to -30 C, 0-6-km shear vector, and the freezing level height.  Large CAPE in the layer from -10 C to -30 C favors rapid hail growth.  0-6-km shear in excess \
            of 30-40 knots supports supercells with persistent updrafts that contribute to large hail production.  Finally, lower freezing level heights suggest a greater probability of \
            hail reaching the surface prior to melting, though melting impacts small hail much more than very large hailstones.</div>',

            'qlcs1': '<div class="spc-prod">0-3 km Bulk Shear (kt) and Theta-e Differential (C), with MUCAPE (J/kg)</div><div class="spc-info">This combination parameter plot attempts \
            to highlight areas potentially favorable for QLCS mesovortex generation.  The three plotted ingredients are 1) 0-3-km bulk shear vector (kt), 2) 0-3-km maximum \
            theta-e difference (C), and 3) MUCAPE (J/kg).  Areas with substantial buoyancy and line-normal bulk shear (30 kt or greater) favor deep upright convection over the gust \
            front of a QLCS, while the theta-e difference infers the potential strength of the cold pool. <br><br>Strong surges in the cold pool (often denoted by bowing segments of a \
            QLCS), when coincident with substantial buoyancy and strong line-normal shear, can favor stretching of vorticity generated along the gust front, and subsequent \
            mesovortex formation.</div><div class="spc-ref"><br>Additional information <a href="https://ams.confex.com/ams/26SLS/webprogram/Manuscript/Paper212008/SchaumannSLS2012_P142.pdf">HERE</a>.</div>',

            'qlcs2': '<div class="spc-prod">0-3 km Bulk Shear (kt) and Theta-e Differential (C), with 100 mb MLCAPE (J/kg)</div><div class="spc-info">This combination parameter plot \
            attempts to highlight areas potentially favorable for QLCS mesovortex generation.  The three plotted ingredients are 1) 0-3-km bulk shear vector (kt), 2) 0-3-km \
            maximum theta-e difference (C), and 3) MUCAPE (J/kg).  Areas with substantial buoyancy and line-normal bulk shear (30 kt or greater) favor deep upright convection over \
            the gust front of a QLCS, while the theta-e difference infers the potential strength of the cold pool. Strong surges in the cold pool (often denoted by bowing segments \
            of a QLCS), when coincident with substantial buoyancy and strong line-normal shear, can favor stretching of vorticity generated along the gust front, and subsequent \
            mesovortex formation.</div><div class="spc-info"><br>Additional information <a href="https://ams.confex.com/ams/26SLS/webprogram/Manuscript/Paper212008/SchaumannSLS2012_P142.pdf">HERE</a>.</div>',

            // Heavy Rain

            'pwtr': '<div class="spc-prod">Precipitable Water (inches)</div><div class="spc-info">Precipitable Water (inches). Values > 1 inch shaded green. Consider \
            values and anomalies for the time of year.</div>',

            'tran': '<div class="spc-prod">850 mb Moisture Transport</div><div class="spc-info">The 850 mb moisture transport is the product of the wind speed \
            (m s<sup>-1</sup>) and the mixing ratio (g g<sup>-1</sup>) at 850 mb.  Values are scaled by factor of 100, such that a 40 kt (~20 m s<sup>-1</sup>) \
            wind speed and a 12 g kg<sup>-1</sup> mixing ratio (0.012 g g<sup>-1</sup>) results in a moisture transport of 24 m s<sup>-1</sup> (the first pink \
            shade in the color fill). High values of moisture transport have been related to heavy rainfall potential with convective systems. </div><div class="spc-info"> \
            Reference:<br> Junker, N. M., R. S. Schneider, and S. L. Fauver, 1999: A study of heavy rainfall events during the great Midwest flood of 1993.  Wea. Forecasting, 14, 701-712.</div>',

            'tran_925': '<div class="spc-prod">925 mb Moisture Transport</div><div class="spc-info">The 925 mb moisture transport is the product of the wind speed \
            (m s<sup>-1</sup>) and the mixing ratio (g g<sup>-1</sup>) at 925 mb.  Values are scaled by factor of 100, such that a 40 kt (~20 m s<sup>-1</sup>) \
            wind speed and a 12 g kg<sup>-1</sup> mixing ratio (0.012 g g<sup>-1</sup>) results in a moisture transport of 24 m s<sup>-1</sup> (the first pink \
            shade in the color fill). High values of moisture transport have been related to heavy rainfall potential with convective systems. </div><div class="spc-info"> \
            Reference:<br> Junker, N. M., R. S. Schneider, and S. L. Fauver, 1999: A study of heavy rainfall events during the great Midwest flood of 1993.  Wea. Forecasting, 14, 701-712. </div> ',

            'prop': '<div class="spc-prod">Upwind Propagation</div><div class="spc-info">The upwind "vector approach" is a method developed by Corfidi et al. (1996) to forecast \
            MCS (or more specifically mesoscale beta element - MBE) movement. It is the vector sum of the mean flow through the cloud-bearing layer and the propagation component. \
            The magnitude and direction of the propagation component is assumed to be equal and opposite to that of the low-level jet (850 mb). </div><div class="spc-info"> \
            Reference:<br> Corfidi, S. F., J. H. Merritt and J. M. Fritsch, 1996: Predicting the movement of mesoscale convective complexes. Wea. Forecasting,11, 41-46. </div> ',

            'peff': '<div class="spc-prod">Precipitation Potential Placement<div class="spc-info">Precipitation Potential Placement is a derived parameter combining \
            precipitable water and low-level mean RH to help better place where rainfall will occur. Research has been published in the National Weather Association Digest in \
            2003 and stems from research and operational use of this product originally developed at NESDIS and Rod Scofield for satellite rainfall estimates dating back to 1981. \
            Rainfall is usually maximized where the best low level convergence and instability overlay with the highest values for this parameter. The risk for heavy rainfall \
            increases as values go up.  Additionally, thresholds for precipitation also change based on temperatures.  Onset of rainfall ranges from around 0.3 inches with \
            temperatures below 30 to 1.0 inches above 80.  Values above 1.0-1.4 inches with temperatures below 60 usually increase the risk for heavy rainfall while values \
            above 1.6-2.0 inches increase the risk for heavy rainfall events with temperatures above 60. </div><div class="spc-info"> \
            For more information, see: http://www.srh.noaa.gov/ffc/research/finalPP2.htm </div>',

            // Winter Weather

            'snsq': '<div class="spc-prod">Snow Squall Parameter</div><div class="spc-info">A non-dimensional composite parameter \
            that combines 0-2 km AGL relative humidity,  0-2 km AGL potential instability (theta-e decreases with height), \
            and 0-2 km AGL mean wind speed (m/s). The intent of the parameter is to identify areas with low-level potential \
            instability, sufficient moisture, and strong winds to support snow squall development.  Surface potential temperatures \
            (theta) and MSL pressure are also plotted to identify strong baroclinic zones which often provide the focused low-level \
            ascent in cases of narrow snow bands. The index is formulated as follows: <br><br>\
            Snow Squall = ((0-2km mean RH - 60%) / 15%) * (( 4 - 2km_delta_theta-e) / 4) * (0-2km mean wind / 9 m s<sup>-1</sup>)<br><br>\
            The 2km_delta_theta-e term is the change in theta-e (K) from the surface to 2km AGL, where negative values represent \
            potential instability.  Areas with 0-2 km RH < 60% are filtered out in the color fill plots.<br><br>\
            <div class="spc-ref">Additional information can be found <a href="http://www.squallwx.com/snowsqualls">here</a> \
            (PowerPoint presentation).</div>',

            'dend': '<div class="spc-prod">Dendritic Layer Depth</div><div class="spc-info">The depth of the dendritic layer \
            (defined here as the layer with temperatures from -12 to -17 C) in meters. Deeper dendritic layer depths may correspond \
            to greater snowfall rates, assuming no melting layers below. Please keep in mind that these real-time fields \
            reflect the 1-h RAP model forecast of temperature, and are subject to any biases in the model forecast itself.</div>',

            'dendrh': '<div class="spc-prod">Dendritic Layer RH and Omega</div><div class="spc-info">The relative humidity (RH) and \
            upward vertical motion (Omega) are displayed for the dendritic growth layer (defined here as the layer with temperatures \
            from -12 to -17 C). Strong ascent and saturated conditions in this layer supports rapid growth of dendritic cyrstals, \
            which favors heavy snow production. Potential melting below the dendritic layer must be considered when evaluating snowfall \
            potential. Also, please keep in mind that these real-time fields reflect the 1-h RAP model forecast of temperature, moisture, and \
            omega aloft, and are subject to any biases in the model forecast itself.</div>',

            // Fire

            'sfir': 'No description',

            'fosb': '<div class="spc-prod">Fosberg Index</div><div class="spc-info">The FWI (Fire Weather Index) is defined by a quantitative \
            model that provides a nonlinear filter of meteorological data which results in a linear relationship between the combined \
            meteorological variables of relative humidity and wind speed, and the behavior of wildfires. Thus the index deals with \
            only the weather conditions, not the fuels. Several sets of conditions have been defined by Fosberg (Fosberg, 1978) \
            to apply this to fire weather management. The upper limits have been set to give an index value of 100 if the moisture \
            content is zero and the wind is 30 mph. Thus, the numbers range from 0 to 100 and if any number is larger than 100, \
            it is set back to 100. The index can be used to measure changes in fire weather conditions. Over several years of use, \
            Fosberg index values of 50 or greater generally appear significant on a national scale. The SPC fire weather \
            verification scheme uses the Fosberg Index, but with a check for both temperature (60F) and adjective fire danger rating \
            (3-High, 4-Very High, 5-Extreme). Fosberg index values are displayed in increments of 10 starting at 50 through \
            100 with the color pink indicating values of 50 or 60, dark orange indicating values of 70 or 80, while values of \
            90 and 100 are shown in bright orange. <br>The Fosberg Index, orginially called the Fire Weather Index (Fosberg, 1978), \
            was created to meet management needs for timeliness of weather information and for a meaningful interpretation of the \
            short time and close space weather impacts on fire management. It is a non-linear filter of meteorological data \
            developed by first transforming temperature and relative humidity to equilibrium moisture content, then \
            transforming the equilibrium moisture content to combustion efficiency. The index is approximated by \
            F = D((Rate of Spread) (Energy Release)) ^0.46 </div>',

            'lhan': '<div class="spc-prod">Haines Index</div><div class="spc-info">This is a fire weather index based on the stability \
            and moisture content of the lower atmosphere that measures the potential for existing fires to become large fires \
            (although this is not a predictor of fire starts). Orange will indicate Haines index values of 4 (low), dark orange \
            will show Haines index values of 5 (moderate), and red will depict Haines index values of 6 (high). Values of 4 and \
            above are plotted on each map even though the overall Haines index is from 2 to 6, with six being the highest potential \
            for large fires (see table below). It is calculated by determining the sum the atmospheric stability index (term A) \
            and the lower atmospheric dryness index (term B). The stability index is determined from measurements of the temperature \
            difference between two atmospheric levels and the dryness index is determined from measurements of the dew-point depression.<br>\
            Due to large variations in elevation across the United States, the index is calculated for three different pressure ranges: \
            low elevation is 950-850mb; mid elevation is 850-700mb; and high elevation is 700-500mb. It is named after its developer, \
            Donald Haines, a Forest Service research meteorologist, who did the initial work and published the scale in 1988.</div> ',

            'lasi': 'No description',

            // Satellite

            'ch01i': '<div class="sat-prod">Visible - CH01 (0.47 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band01.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch02i': '<div class="sat-prod">Visible - CH02 (0.64 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band02.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch03i': '<div class="sat-prod">Veggie Band - CH03 (0.86 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band03.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch04i': '<div class="sat-prod">Cirrus Band - CH04 (1.37 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band04.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch05i': '<div class="sat-prod">Snow/Ice Band - CH05 (1.61 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band05.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch06i': '<div class="sat-prod">Cloud Particle Size Band - CH06 (2.24 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band05.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch07i': '<div class="sat-prod">Shortwave (Near) IR Band - CH07 (3.9 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band05.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch08i': '<div class="sat-prod">Upper Level Water Vapor - CH08 (6.2 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band08.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch09i': '<div class="sat-prod">Mid Level Water Vapor - CH09 (6.9 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band09.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch10i': '<div class="sat-prod">Mid Level Water Vapor - CH10 (7.3 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band10.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch11i': '<div class="sat-prod">Infrared Cloud Phase - CH11 (8.5 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band11.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',
            
            'ch12i': '<div class="sat-prod">Ozone Band - CH12 (9.6 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band12.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch13i': '<div class="sat-prod">Clean Longwave Infrared Window - CH13 (10.3 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band13.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch14i': '<div class="sat-prod">Infrared Longwave Window - CH14 (11.2 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band14.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch15i': '<div class="sat-prod">Dirty Window Band - CH15 (12.3 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band15.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'ch16i': '<div class="sat-prod">CO2 Band - CH16 (13.3 um)</div><div class="sat-info">Click <a \
            href="http://cimss.ssec.wisc.edu/goes/OCLOFactSheetPDFs/ABIQuickGuide_Band16.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'geoci': '<div class="sat-prod">CIRA GeoColor RGB</div><div class="sat-info">Click <a \
            href="https://rammb.cira.colostate.edu/training/visit/quick_guides/QuickGuide_CIRA_Geocolor_20171019.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'nmici': '<div class="sat-prod">Nighttime Microphysics RGB</div><div class="sat-info">Click <a \
            href="https://rammb.cira.colostate.edu/training/visit/quick_guides/QuickGuide_GOESR_NtMicroRGB_Final_20191206.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'airmi': '<div class="sat-prod">Airmass RGB</div><div class="sat-info">Click <a \
            href="https://rammb.cira.colostate.edu/training/visit/quick_guides/QuickGuide_GOESR_AirMassRGB_final.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'sandi': '<div class="sat-prod">Sandwich Product</div><div class="sat-info">Click <a \
            href="https://www.star.nesdis.noaa.gov/goes/documents/SandwichProduct.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

            'firti': '<div class="sat-prod">Fire Temperature RGB</div><div class="sat-info">Click <a \
            href="https://rammb.cira.colostate.edu/training/visit/quick_guides/Fire_Temperature_RGB.pdf" target="_blank">HERE</a> to open quick guide pdf in another tab</div>',

        }

        //const sat_loops = ['ch02', 'ch07', 'ch08', 'ch13', 'ch14', 'geoc', 'airm', 'sand', 'nmic', 'dayp', 'firt']
        descriptions['trap_500'] = descriptions['trap']
        descriptions['trap_250'] = descriptions['trap']
        descriptions['tran_925-850'] = descriptions['tran_925']
        descriptions['srh3'] = descriptions['srh1']
        descriptions['alsr'] = descriptions['ulsr']
        descriptions['mhan'] = descriptions['lhan']
        descriptions['hhan'] = descriptions['lhan']


        descriptions['conus-ch02'] = descriptions['ch02i']
        descriptions['sector-ch02'] = descriptions['ch02i']
        descriptions['conus-ch07'] = descriptions['ch07i']
        descriptions['sector-ch07'] = descriptions['ch07i']
        descriptions['conus-ch08'] = descriptions['ch08i']
        descriptions['sector-ch08'] = descriptions['ch08i']
        descriptions['conus-ch13'] = descriptions['ch13i']
        descriptions['sector-ch13'] = descriptions['ch13i']
        descriptions['conus-ch14'] = descriptions['ch14i']
        descriptions['sector-ch14'] = descriptions['ch14i']
        descriptions['conus-geoc'] = descriptions['geoci']
        descriptions['sector-geoc'] = descriptions['geoci']
        descriptions['conus-airm'] = descriptions['airmi']
        descriptions['sector-airm'] = descriptions['airmi']
        descriptions['conus-sand'] = descriptions['sandi']
        descriptions['sector-sand'] = descriptions['sandi']
        descriptions['conus-nmic'] = descriptions['nmici']
        descriptions['sector-nmic'] = descriptions['nmici']
        descriptions['conus-firt'] = descriptions['firti']
        descriptions['sector-firt'] = descriptions['firti']
    </script>
</body>

</html>
"""

title = dbc.Container([
        html.Br(),
        dbc.Row([dbc.Col(html.H2("SPC Mesoanalysis"), width=12)])
    ])


mesoanalysis = dbc.Container([
      dbc.Row([
          dbc.Col(
              html.Iframe(
                  srcDoc=EMBEDDED_HTML,
                  style={'width': '100%', 'height': '980px'}
              )
          )
        ],style={'padding':'0.5em'}),
            ])

# Define the page layout
def layout():
    """mesoanalysis page layout

    Returns:
        None
    """
    return dbc.Container([title, mesoanalysis])
