from pathlib import Path

DATA_DIRECTORY = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    DATA_DIRECTORY = 'C:/data/scripts/pyany/data'

BUOY_DICT = {'45024': {'title': 'Ludington Buoy', 'row': 1},           
         '45161': {'title': 'Muskegon Buoy', 'row': 2},
         '45029': {'title': 'Holland Buoy', 'row': 3},
         '45168': {'title': 'South Haven Buoy', 'row': 4},
         '45210': {'title': 'Central LM', 'row': 5},
         '45007': {'title': 'LM South Buoy', 'row': 6}
}

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