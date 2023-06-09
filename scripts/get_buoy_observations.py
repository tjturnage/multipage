"""
This gets the buoy data from the NDBC website
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd


cwd = Path().absolute()
data_directory = cwd.parent / 'data'


ELEMENT_NAMES = ['WDIR','WSPD','WGST','WVHT']
ELEMENT_DICT = {'WDIR': 0, 'WSPD': 1, 'WGST': 2, 'WVHT': 3}
METERS_PER_SECOND_TO_KNOTS = 1.94384
METERS_TO_FEET = 3.280
BASE_URL = 'https://www.ndbc.noaa.gov/data/realtime2'

BUOY_NAMES = {'45024': 'Ludington Buoy',
        'LDTM4': 'Ludington',
        '45161': 'Muskegon Buoy',
        'MKGM4': 'Muskegon',
        '45029': 'Holland Buoy',
        'HLNM4': 'Holland',
        '45168': 'South Haven Buoy',
        'SVNM4': 'South Haven',
        '45210': 'Central LM',
        '45007': 'LM South Buoy'
}

BUOY_IDS = list(BUOY_NAMES.keys())

@dataclass
class BuoyDataFrames:
    df_45024: pd.DataFrame
    df_ldtm4: pd.DataFrame
    df_45161: pd.DataFrame
    df_mkgm4: pd.DataFrame
    df_45029: pd.DataFrame
    df_hlnm4: pd.DataFrame
    df_45168: pd.DataFrame
    df_svnm4: pd.DataFrame
    df_45210: pd.DataFrame
    df_45007: pd.DataFrame


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
            '45210': self.df_45210,
            '45007': self.df_45007
            }
        self.max_height, self.max_speed = 0,0
        self.upper_height, self.upper_speed = 0,0
        self.now = datetime.utcnow()
        self.start = self.now - timedelta(hours=3)
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
            #short_df = this_df.loc[this_df['dts'] > start]

            destination = data_directory / f'{buoy}.csv'  
            this_df.to_csv(destination, index=False)

        return


if __name__ == '__main__':
    BuoyData()
