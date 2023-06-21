"""
05 Jan 2020: Now importing API_TOKEN for privacy since data are proprietary
25 Feb 2023: Included RWIS data

Retrieves observations via the Mesowest API.
Learn more about setting up your own account at: https://synopticdata.com/

Get latest obs: https://developers.synopticdata.com/mesonet/v2/stations/latest/
Obs network/station providers: https://developers.synopticdata.com/about/station-providers
Selecting stations: https://developers.synopticdata.com/mesonet/v2/station-selectors/

"""

import os
import math
from datetime import datetime, timedelta
import requests

try:
    os.listdir('/home/tjturnage')
    DEST_HOME = '/home/tjturnage/multipage/assets'
except FileNotFoundError:
    DEST_HOME = 'C:/data'


#DEST_HOME = '/home/tjt/public_html/public/placefiles'
#DEST_HOME = 'C:/data/scripts/mesowest'

#dstFile = '/home/tjt/public_html/public/placefiles/latest_surface_observations.txt'
#dstFile = 'latest_surface_observations.txt'

#from api_tokens import mesowest_API_TOKEN as API_TOKEN
API_TOKEN = "292d36a692d74badb6ca011f4413ae1b"  # placeholder for testing
API_ROOT = "https://api.synopticdata.com/v2/"

def time_shift(time_str,num,d_t,direction='backward',api='mesowest'):
    """
    Returns list of timestrings associated with a list of time intervals

    Parameters
    ----------
          timeStr : string
                    'YYYYmmddHHMM' format
              num : integer
                    number of time steps
               dt : integer
                    number of minutes per step
        direction : string
                    'backward'       - step back in time from timeStr
                    <anything else>  - step forward in time from timeStr
              api : string
                    'mesowest'       - format needed for mesowest api request
                                       Example: '2020-01-10T06:35:12Z'
                                        
                    'mping'          - format needed for mping api request
                                       Example: '2020-01-10 06:35:12'
            
    Returns
    -------
            times : list
                    list of time intervals. These intervals contain 3 elements:
                    - interval start time string as 'YYYYmmddHHMM'
                    - interval start time string using either mesowest or mping format
                    - interval end time string using either mesowest or mping format                    


    """
    times = []
    steps = int(num)
    min_start = int(steps * d_t)
    init_time = datetime.strptime(time_str,'%Y%m%d%H%M')
    if direction == 'backward':
        orig_time = init_time - timedelta(minutes=min_start)
    else:
        orig_time = init_time

    for step in range(0,steps):
        mins = step * d_t
        new_time = orig_time + timedelta(minutes=mins)
        next_time = new_time + timedelta(minutes=d_t)
        new_str = datetime.strftime(new_time, '%Y%m%d%H%M')
        if api == 'mesowest':
            new = datetime.strftime(new_time, '%Y-%m-%dT%H:%M:%SZ')
            next_time_str = datetime.strftime(next_time, '%Y-%m-%dT%H:%M:%SZ')
        else:
            new = datetime.strftime(new_time, '%Y-%m-%d %H:%M:%S')
            next_time_str = datetime.strftime(next_time, '%Y-%m-%d %H:%M:%S')
        times.append([new_str,new,next_time_str])
    return times



class Mesowest():
    """
    Need to put something in here

    """

    def __init__(self,bbox="-90.5,40,-82,47",event_time=None):

        self.bbox = bbox
        self.event_time = event_time
        self.d_t = 10 # number of minutes to increment
        self.steps = 18 # number of increments
        self.network = "1,2,96,162"
        self.var_str = 'air_temp,dew_point_temperature,wind_speed,wind_direction,wind_gust,visibility,road_temp'
        self.unit_str = 'temp|F,speed|kts,precip|in'
        self.api_args = {"token":API_TOKEN,
                        "bbox":self.bbox,
                        "status":"active",
                        "network":self.network,
                        "vars":self.var_str,
                        "units":self.unit_str,
                        "within":"30"}

        if self.event_time is None:
            now = datetime.utcnow()
            round_down = now.minute%5
            round_up = 10 - round_down
            self.base_time = now + timedelta(minutes=round_up)
            self.place_time = now - timedelta(minutes=round_down)
            self.place_ts = datetime.strftime(self.place_time,'%Y%m%d%H%M')
        else:
            self.base_time = datetime.strptime(self.event_time,'%Y%m%d%H%M')
            self.place_ts = self.event_time

        self.base_ts = datetime.strftime(self.base_time,'%Y%m%d%H%M')

        self.times = time_shift(self.base_ts,self.steps,self.d_t,'backward','mesowest')

        self.short_dict = {'air_temp_value_1':'t',
                    'dew_point_temperature_value_1d':'dp',
                    'wind_speed_value_1':'wspd',
                    'wind_direction_value_1':'wdir',
                    'wind_gust_value_1':'wgst',
                    'visibility_value_1':'vis',
                    'road_temp_value_1': 'rt'
                    }

        self.var_list = list(self.short_dict.keys())
        wind_zoom = 500
        rwis_wind_zoom = 300
        t_zoom = 300
        rwis_t_zoom = 200
        gray = '180 180 180'
        white= '255 255 255'
        self.stn_dict2 = {'t':{'threshold':t_zoom,'color':'225 75 75','position':'-17,13, 1,'},
                'dp':{'threshold':t_zoom,'color':'0 255 0','position':'-17,-13, 1,'},
                'wspd':{'threshold':wind_zoom,'color':white,'position':'NA'},
                'wdir':{'threshold':wind_zoom,'color':white,'position':'NA'},
                'wgst':{'threshold':wind_zoom,'color':white,'position':'NA'},
                'vis':{'threshold':100,'color':'180 180 255','position':'17,-13, 1,'},
                'rt':{'threshold':500,'color':'255 255 0','position':'17,13, 1,'}}

        self.rwis_dict = \
            {'t':{'threshold':rwis_t_zoom,'color':'200 100 100','position':'-17,13, 2,'},
            'dp':{'threshold':rwis_t_zoom,'color':'25 225 25','position':'-17,-13, 2,'},
            'wspd':{'threshold':rwis_wind_zoom,'color':gray,'position':'NA'},
            'wdir':{'threshold':rwis_wind_zoom,'color':gray,'position':'NA'},
            'wgst':{'threshold':rwis_wind_zoom,'color':gray,'position':'NA'},
            'vis':{'threshold':100,'color':'180 180 255','position':'17,-13, 2,'},
            'rt':{'threshold':500,'color':'255 255 0','position':'17,13, 2,'}}

        place_text = \
        f'{self.place_ts[0:4]}-{self.place_ts[4:6]}-{self.place_ts[6:8]}-{self.place_ts[-4:]}'
        self.all_title = f'All Elements {place_text}'
        self.place_title = f'Air Temperature {place_text}'
        self.wind_place_title = f'Wind and Gust {place_text}'
        self.road_place_title = f'Road Temperature {place_text}'
        self.dewpoint_place_title = f'Dewpoint Temperature {place_text}'
        self.build_placefile()

    def str_to_fl(self,string):
        """
        Tries to convert string to float. If unsuccessful, returns 'NA' string
        """
        try:
            return float(string)
        except Exception:
            return 'NA'

    def build_placefile(self):
        """
        go through the steps
        """
        icon_stuff = 'IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n '

        self.placefile = 'Title: Mesowest ' + self.place_title + '\nRefresh: 1\nColor: 255 200 255\n \
        IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n \
        Font: 1, 14, 1, "Arial"\n \
        Font: 2, 11, 1, "Arial"\n\n'

        self.wind_placefile = 'Title: Mesowest ' + self.wind_place_title + '\nRefresh: 1\nColor: 255 200 255\n \
        IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n \
        Font: 1, 14, 1, "Arial"\n \
        Font: 2, 11, 1, "Arial"\n\n'

        self.road_placefile = 'Title: Mesowest ' + self.road_place_title + '\nRefresh: 1\nColor: 255 200 255\n \
        IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n \
        Font: 1, 14, 1, "Arial"\n \
        Font: 2, 11, 1, "Arial"\n\n'
        
        self.dewpoint_placefile = 'Title: Mesowest ' + self.dewpoint_place_title + '\nRefresh: 1\nColor: 255 200 255\n \
        IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n \
        Font: 1, 14, 1, "Arial"\n \
        Font: 2, 11, 1, "Arial"\n\n'

        self.all_placefile = 'Title: Mesowest ' + self.all_title + '\nRefresh: 1\nColor: 255 200 255\n \
        IconFile: 1, 18, 32, 2, 31, "https://mesonet.agron.iastate.edu/request/grx/windbarbs.png" \n \
        IconFile: 2, 15, 15, 8, 8, "https://mesonet.agron.iastate.edu/request/grx/cloudcover.png"\n \
        IconFile: 3, 25, 25, 12, 12, "https://mesonet.agron.iastate.edu/request/grx/rwis_cr.png"\n \
        Font: 1, 14, 1, "Arial"\n \
        Font: 2, 11, 1, "Arial"\n\n'


        for _t,this_time in enumerate(self.times):
            time_str = this_time[0]
            jas = self.mesowest_get_nearest_time_data(time_str)
            now = this_time[1]
            future = this_time[2]

            #Example of TimeRange line:
            #TimeRange: 2019-03-06T23:14:39Z 2019-03-06T23:16:29Z

            time_text = f'TimeRange: {now} {future}\n\n'
            self.placefile += time_text
            self.wind_placefile += time_text
            self.road_placefile += time_text
            self.dewpoint_placefile += time_text
            self.all_placefile += time_text
            for j,station in enumerate(jas['STATION']):
                temp_txt = ''
                lon = (station['LONGITUDE'])
                lat = (station['LATITUDE'])
                status = (station['STATUS'])
                network = (int(station['MNET_ID']))
                if int(network) == 162:
                    wind_zoom = 300
                else:
                    wind_zoom = 500
                t_txt = ''
                dp_txt = ''
                t_str = 'NA'
                dp_str = 'NA'
                wdir_str = 'NA'
                wspd_str = 'NA'
                wgst_str = 'NA'
                vis_txt = ''
                vis_str = 'NA'
                rt_txt = ''
                rt_str = 'NA'
                if status == 'ACTIVE':
                    for _n,element in enumerate(self.var_list):
                        short = str(self.short_dict[element])
                        try:
                            scratch = jas['STATION'][j]['OBSERVATIONS'][element]['value']
                            if short == 't':
                                t_str, text_info = self.convert_met_values(scratch,short,network)
                                t_txt = temp_txt + text_info
                            elif short == 'dp':
                                dp_str, text_info = self.convert_met_values(scratch,short,network)
                                dp_txt = temp_txt + text_info
                            elif short == 'rt':
                                rt_str, text_info = self.convert_met_values(scratch,short,network)
                                rt_txt = temp_txt + text_info
                            elif short == 'vis':
                                if int(network) != 162:
                                    vis_str, text_info = \
                                    self.convert_met_values(scratch,short,network)
                                    vis_txt = temp_txt + text_info
                                else:
                                    pass
                            elif short == 'wspd':
                                wspd_str, _val = self.convert_met_values(scratch,short,network)
                            elif short == 'wdir':
                                wdir_str, _val = self.convert_met_values(scratch,short,network)
                            elif short == 'wgst':
                                wgst_str, text_info = self.convert_met_values(scratch,short,network)
                                #wgst_txt = temp_txt + text_info

                        except ValueError as value_error:  # Catch only ValueErrors
                            print(f"Caught a ValueError: {value_error}")
                            pass
                        except TypeError as type_error:  # Catch only TypeErrors
                            print(f"Caught a TypeError: {type_error}")
                            pass
                        except Exception as exception:   # Use a general exception handler as a "catch all"
                            #print(f"Caught an unexpected error: {exception}")
                            pass


                obj_head = f'Object: {lat},{lon}\n'

                if wdir_str != 'NA' and wspd_str != 'NA':
                    self.all_placefile += f'{obj_head}  Threshold: {wind_zoom}\n  Icon: 0,0,{wdir_str},1,{wspd_str}\n End:\n\n'
                    self.wind_placefile += f'{obj_head}  Threshold: {wind_zoom}\n  Icon: 0,0,{wdir_str},1,{wspd_str}\n End:\n\n'

                if t_str != 'NA':
                    self.all_placefile += f'{obj_head}{t_txt} End:\n\n'
                    self.placefile += f'{obj_head}{t_txt} End:\n\n'
                if dp_str != 'NA':
                    self.all_placefile += f'{obj_head}{dp_txt} End:\n\n'
                    self.dewpoint_placefile += f'{obj_head}{dp_txt} End:\n\n'

                if wgst_str != 'NA' and wdir_str != 'NA':
                    wgst_text = self.gust_obj(wdir_str, int(wgst_str), 'wgst', network)
                    self.all_placefile += f'{obj_head}{wgst_text} End:\n\n'
                    self.wind_placefile += f'{obj_head}{wgst_text} End:\n\n'
                if vis_str != 'NA':
                    self.placefile += f'{obj_head}{vis_txt} End:\n\n'
                if rt_str != 'NA':
                    self.all_placefile += f'{obj_head}{rt_txt} End:\n\n'
                    self.road_placefile += f'{obj_head}{rt_txt} End:\n\n'


        with open(os.path.join(DEST_HOME, 'temp.txt'), 'w', encoding='utf8') as outfile:
            outfile.write(self.placefile)

        with open(os.path.join(DEST_HOME, 'wind.txt'), 'w', encoding='utf8') as outfile:
            outfile.write(self.wind_placefile)

        with open(os.path.join(DEST_HOME, 'road.txt'), 'w', encoding='utf8') as outfile:
            outfile.write(self.road_placefile)

        with open(os.path.join(DEST_HOME, 'dwpt.txt'), 'w', encoding='utf8') as outfile:
            outfile.write(self.dewpoint_placefile)

        with open(os.path.join(DEST_HOME, 'latest_surface_observations.txt'), 'w', encoding='utf8') as outfile:
            outfile.write(self.all_placefile)

    def mesowest_get_nearest_time_data(self,time_str):
        """
        Mesowest API request for data at the nearest available time defined by a time string.

        Parameters
        ----------
            timeStr : string
                      format is YYYYmmDDHHMM (ex. 202002290630)
        Returns
        -------
               jas : json file
                      observational data
        """
        api_request_url = os.path.join(API_ROOT, "stations/nearesttime")
        self.api_args['attime'] = time_str
        req = requests.get(api_request_url, params=self.api_args, timeout=30)

        jas = req.json()
        return jas

    def placefile_wind_speed_code(self,wspd):
        """
        Returns the proper code for plotting wind speeds in a GR2Analyst placefile. 
        This code is then used for the placefile IconFile method described at:
            http://www.grlevelx.com/manuals/gis/files_places.htm
        
        Parameters
        ----------
                wspd : string
                        wind speed in knots
                                            
        Returns
        -------
                code : string
                        string of integer to be used to reference placefile icon

        """
        speed = float(wspd)
        if speed > 52:
            code = '11'
        elif speed > 47:
            code = '10'
        elif speed > 42:
            code = '9'
        elif speed > 37:
            code = '8'
        elif speed > 32:
            code = '7'
        elif speed > 27:
            code = '6'
        elif speed > 22:
            code = '5'
        elif speed > 17:
            code = '4'
        elif speed > 12:
            code = '3'
        elif speed > 7:
            code = '2'
        elif speed > 2:
            code = '1'
        else:
            code = '1'

        return code

    def convert_met_values(self,num,short,network):
        """_summary_

        Args:
            num (_type_): _description_
            short (_type_): _description_
            network (_type_): _description_

        Returns:
            _type_: _description_
        """
        numfloat = float(num)
        if (num != 'NA' ):
            if (short == 't') or (short == 'dp') or (short == 'rt'):
                new = int(round(numfloat))
                new_str = '" ' + str(new) + ' "'
                text_info = self.build_object(new_str,short,network)
            elif short == 'wgst':
                new = int(round(numfloat,1))
                new_str = '" ' + str(new) + ' "'    
                text_info = self.build_object(new_str,short,network)
                new_str = str(new)
            elif short == 'vis':
                #print (numfloat)
                final = '10'
                if numfloat < 6.5:
                    final = str(int(round(numfloat)))
                if numfloat <= 2.75:
                    final = '2 3/4'
                if numfloat <= 2.50:
                    final = '2 1/2'
                if numfloat <= 2.25:
                    final = '2 1/4'
                if numfloat <= 2.0:
                    final = '2'
                if numfloat <= 1.75:
                    final = '1 3/4'
                if numfloat <= 1.50:
                    final = '1 1/2'                 
                if numfloat <= 1.25:
                    final = '1 1/4'
                if numfloat <= 1.00:
                    final = '1'
                if numfloat <= 0.75:
                    final = '3/4'
                if numfloat <= 0.50:
                    final = '1/2'
                if numfloat <= 0.25:
                    final = '1/4'
                if numfloat <= 0.125:
                    final = '1/8'
                if numfloat == 0.0:
                    final = ''
                new_str = '" ' + final + ' "'
                text_info = self.build_object(new_str,short,network)
            elif short == 'wspd':
                new = self.placefile_wind_speed_code(numfloat)
                new_str = str(new)
                text_info = 'ignore'
            elif short == 'wdir':
                new = int(num)
                new_str = str(new)
                text_info = 'ignore'

            return new_str, text_info

    def gust_obj(self,wdir, wgst, short,network):
        """_summary_

        Args:
            wdir (_type_): _description_
            wgst (_type_): _description_
            short (_type_): _description_
            network (_type_): _description_

        Returns:
            _type_: _description_
        """
        if int(network) == 162:
            font_code = 2
            this_dict = self.rwis_dict
        else:
            font_code = 1
            this_dict = self.stn_dict2


        distance = 35
        wgst_int = int(wgst)
        new_str = '" ' + str(wgst_int) + ' "'
        direction = int(wdir)
        x = int(math.sin(math.radians(direction)) * distance)
        y = int(math.cos(math.radians(direction)) * distance)
        loc = f'{x},{y}, {font_code},'
        thresh_line = 'Threshold: ' + str(this_dict[short]['threshold']) + '\n'
        color_line = '  Color: ' + str(this_dict[short]['color']) + '\n'
        position = '  Text: ' + loc + new_str + ' \n'
        text_info = thresh_line + color_line + position
        return text_info

    def build_object(self,new_str,short,network):
        """_summary_

        Args:
            new_str (_type_): _description_
            short (_type_): _description_
            network (_type_): _description_

        Returns:
            _type_: _description_
        """
        if int(network) == 162:
            this_dict = self.rwis_dict
        else:
            this_dict = self.stn_dict2
        
        thresh_line = 'Threshold: ' + str(this_dict[short]['threshold']) + '\n'
        color_line = '  Color: ' + str(this_dict[short]['color']) + '\n'
        position = '  Text: ' + str(this_dict[short]['position']) + new_str + '\n'
        text_info = thresh_line + color_line + position
        return text_info




if __name__ == "__main__":
    test = Mesowest()
    