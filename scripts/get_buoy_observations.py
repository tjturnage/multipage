"""
This gets the buoy data from the NDBC website
"""
from datetime import datetime, timedelta
import pandas as pd

from config import DATA_DIRECTORY as DEST_DATA_DIRECTORY
from config import BUOY_DICT, METERS_PER_SECOND_TO_KNOTS, METERS_TO_FEET

BASE_URL = 'https://www.ndbc.noaa.gov/data/realtime2'

BUOY_IDS = list(BUOY_DICT.keys())

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
        self.now = datetime.utcnow()
        self.start = self.now - timedelta(hours=4)
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

            destination = f'{DEST_DATA_DIRECTORY}/{buoy}.csv'  
            short_df.to_csv(destination, index=False)

        return


if __name__ == '__main__':
    BuoyData()
