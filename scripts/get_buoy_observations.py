"""
This gets the buoy data from the NDBC website
"""
from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path

BASE_URL = 'https://www.ndbc.noaa.gov/data/realtime2'

DATA_DIRECTORY = '/home/tjturnage/multipage/data'
if 'pyany' in Path().absolute().parts:
    DATA_DIRECTORY = 'C:/data/scripts/pyany/data'

opac = 0.85
lw = 1.5
BUOY_DICT = {'45024': {'title': 'Ludington Buoy', 'color': f'rgba(255, 255, 255, {opac})', 'line_width': lw, 'row': 1},           
         '45161': {'title': 'Muskegon Buoy', 'color': f'rgba(200, 200, 255, {opac})', 'line_width': lw, 'row': 2},
         '45029': {'title': 'Holland Buoy', 'color': f'rgba(150, 150, 255, {opac})', 'line_width': lw, 'row': 3},
         '45168': {'title': 'South Haven Buoy', 'color': f'rgba(112, 112, 255, {opac})', 'line_width': lw, 'row': 4},
         '45026': {'title': 'Cook Nuclear Plant Buoy', 'color': f'rgba(112, 112, 255, {opac})', 'line_width': lw, 'row': 5},
         '45210': {'title': 'Central LM', 'color': f'rgba(80, 80, 255, {opac})', 'line_width': lw, 'row': 5},
         '45007': {'title': 'LM South Buoy', 'color': f'rgba(30, 30, 255, {opac})', 'line_width': lw, 'row': 6}
         }

BUOY_IDS = list(BUOY_DICT.keys())

CMAN_DICT = {'LDTM4': {'title': 'Ludington', 'row': 2},
            'MKGM4': {'title': 'Muskegon', 'row': 4},
            'HLNM4': {'title': 'Holland', 'row': 6},
            'SVNM4': {'title': 'South Haven', 'row': 8},
             }


METERS_PER_SECOND_TO_KNOTS = 1.94384
METERS_TO_FEET = 3.280






class BuoyData():

    def __init__(self):
        self.df_45024 = pd.DataFrame()
        self.df_ldtm4 = pd.DataFrame()
        self.df_45161 = pd.DataFrame()
        self.df_mkgm4 = pd.DataFrame()
        self.df_45029 = pd.DataFrame()
        self.df_hlnm4 = pd.DataFrame()
        self.df_45168 = pd.DataFrame()
        self.df_svnm4 = pd.DataFrame()
        self.df_45026 = pd.DataFrame()
        self.df_45210 = pd.DataFrame()
        self.df_45007 = pd.DataFrame()
        self.buoy_data = {'45024': self.df_45024,
            'LDTM4': self.df_ldtm4,
            '45161': self.df_45161,
            'MKGM4': self.df_mkgm4,
            '45029': self.df_45029,
            'HLNM4': self.df_hlnm4,
            '45168': self.df_45168,
            'SVNM4': self.df_svnm4,
            '45026': self.df_45026,
            '45210': self.df_45210,
            '45007': self.df_45007
            }
        self.now = datetime.utcnow()
        self.start = self.now - timedelta(hours=12)
        self.update_buoy_dict()
    
    
    def update_buoy_dict(self):
        """_summary_
        """

        for buoy in BUOY_IDS:
            this_df = self.buoy_data[buoy]
            url = f'{BASE_URL}/{buoy}.txt'
            this_df = pd.read_csv(url, delim_whitespace=True, skiprows=[1], na_values='MM', nrows=200)

            column_mapping = {'#YY': 'year', 'MM': 'month', 'DD': 'day', 'hh': 'hour', 'mm': 'minute'}
            this_df = this_df.rename(columns=column_mapping)
            this_df = this_df.iloc[:, :-10]
            this_df['dts'] = pd.to_datetime(this_df[['year','month','day','hour','minute']])
            this_df.drop(columns=['year','month','day','hour','minute'], inplace=True)
            this_df['WSPD'] = this_df['WSPD'] * METERS_PER_SECOND_TO_KNOTS
            this_df['GST'] = this_df['GST'] * METERS_PER_SECOND_TO_KNOTS
            this_df['WVHT'] = this_df['WVHT'] * METERS_TO_FEET
            short_df = this_df.loc[this_df['dts'] > self.start]

            destination = f'{DATA_DIRECTORY}/{buoy}.csv'  
            short_df.to_csv(destination, index=False)

        return


if __name__ == '__main__':
    BuoyData()
