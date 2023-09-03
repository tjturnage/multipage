from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd

start = datetime.utcnow() - timedelta(hours=3)



DATA_DIRECTORY = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    DATA_DIRECTORY = 'C:/data/scripts/pyany/data'

opac = 0.99
lw = 3
BUOY_DICT = {'45024': {'title': 'Ludington Buoy', 'color': f'rgba(255, 255, 255, {opac})', 'line_width': lw, 'row': 1},           
         '45161': {'title': 'Muskegon Buoy', 'color': f'rgba(200, 200, 255, {opac})', 'line_width': lw, 'row': 2},
         '45029': {'title': 'Holland Buoy', 'color': f'rgba(150, 150, 255, {opac})', 'line_width': lw, 'row': 3},
         '45168': {'title': 'South Haven Buoy', 'color': f'rgba(112, 112, 255, {opac})', 'line_width': lw, 'row': 4},
         '45026': {'title': 'Cook Nuclear Plant Buoy', 'color': f'rgba(112, 112, 255, {opac})', 'line_width': lw, 'row': 5},
         '45210': {'title': 'Central LM', 'color': f'rgba(80, 80, 255, {opac})', 'line_width': lw, 'row': 6},
         '45007': {'title': 'LM South Buoy', 'color': f'rgba(30, 30, 255, {opac})', 'line_width': lw, 'row': 7}
         }

BUOY_IDS = list(BUOY_DICT.keys())

BUOY_TITLES = []
for key in BUOY_DICT:
    BUOY_TITLES.append(BUOY_DICT[key]['title'])


WINDSPEED_TITLE = 'Wind Speed and Gust (kt)'
WAVE_SUB_PREFIX = '<b><span style="color:#DDDD33;">'
WAVE_SUB_SUFFIX = '</b> Wave Height (ft)'
titles=[]
for b in BUOY_TITLES:
    this_title = f'{WAVE_SUB_PREFIX}{b}{WAVE_SUB_SUFFIX}'
    titles.append(this_title)
    titles.append(WINDSPEED_TITLE)

SUBPLOT_TITLES = tuple(titles)


CMAN_DICT = {'LDTM4': {'title': 'Ludington', 'row': 2},
            'MKGM4': {'title': 'Muskegon', 'row': 4},
            'HLNM4': {'title': 'Holland', 'row': 6},
            'SVNM4': {'title': 'South Haven', 'row': 8},
             }

STYLE_DICT = {'GST': {'line': dict(color='white', width=0), 'marker': dict(color='white', size=3)},
              'WVHT': {'line': dict(color='#00CCCC', width=3), 'marker': dict(color='#00CCCC', size=3)},
              'WSPD': {'line': dict(color='gray', width=3), 'marker': dict(color='gray', size=0)}
              }

METERS_PER_SECOND_TO_KNOTS = 1.94384
METERS_TO_FEET = 3.280

WINDSPEED_TITLE = 'Wind Speed and Gust (kt)'
WAVE_SUB_PREFIX = '<b><span style="color:#DDDD33;">'
WAVE_SUB_SUFFIX = '</b> Wave Height (ft)'

def update_buoys():
    """
    creates a dictionary of dataframes by reading a csv file
    for each buoy id in BUOY_IDS
    """
    this_new_buoy_data = {}
    this_max_height = 0
    this_max_speed = 0
    this_min_height = 100
    this_min_speed = 100
    for buoy in BUOY_IDS:
        this_source = f'{DATA_DIRECTORY}/{buoy}.csv'
        temp_dataframe = pd.read_csv(this_source, parse_dates=['dts'], index_col='dts')
        set_ranges_df = temp_dataframe.loc[temp_dataframe.index > start]
        this_max_height = max(this_max_height, set_ranges_df['WVHT'].max())
        this_max_speed = max(this_max_speed, set_ranges_df['GST'].max())
        this_min_height = min(this_min_height, set_ranges_df['WVHT'].min())
        this_min_speed = min(this_min_speed, set_ranges_df['GST'].min())
        this_new_buoy_data[buoy] = temp_dataframe
    
    this_max_wave = this_max_height + 1
    this_min_wave = this_min_height - 1
    final_min_wave = max(this_min_wave, 0)
    new_max_speed = this_max_speed + 5 - (this_max_speed % 5)
    new_min_speed = this_min_speed - 5 + (this_min_speed % 5)
    final_min_speed = max(new_min_speed, 0)

    return this_new_buoy_data, this_max_wave, final_min_wave, new_max_speed, final_min_speed

def update_times():
    """
    defines the x axis range based on the current time

    Returns:
        start_time: datetime object : xmin for graph
    """
    now = datetime.utcnow()
    start_time = now - timedelta(hours=3)
    end_time = now + timedelta(minutes=10)
    return now, start_time, end_time

