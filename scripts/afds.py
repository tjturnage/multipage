"""_summary_

    Returns:
        _type_: _description_
"""
from datetime import datetime
#from pathlib import Path
import requests
from bs4 import BeautifulSoup

"""
h = Path('/home')

if h.exists():
    p = h / 'tjturnage'
    if p.exists():
        q = p / 'multipage' / 'assets' 
    else:
        q = None
        print("get on pyanwhere!")
else:
    q = Path('assets')
"""

OUTPUT_PATH = '/home/tjturnage/multipage/assets/afds.txt'


UPDATE = True
SYNOPSIS = False
SHORT_TERM = True
LONG_TERM = True
DISCUSSION = True
AVIATION = False
FIRE_WEATHER = False
HYDROLOGY = False
MARINE = False
CLIMATE = False

sections_to_retrieve = []
if UPDATE:
    sections_to_retrieve.append('.UPDATE')
if SYNOPSIS:
    sections_to_retrieve.append('.SYNOPSIS')
if SHORT_TERM:
    sections_to_retrieve.append('.SHORT TERM')
if LONG_TERM:
    sections_to_retrieve.append('.LONG TERM')
if DISCUSSION:
    sections_to_retrieve.append('.DISCUSSION')
if AVIATION:
    sections_to_retrieve.append('.AVIATION')
if FIRE_WEATHER:
    sections_to_retrieve.append('.FIRE WEATHER')
if HYDROLOGY:
    sections_to_retrieve.append('.HYDROLOGY')
if MARINE:
    sections_to_retrieve.append('.MARINE')
if CLIMATE:
    sections_to_retrieve.append('.CLIMATE')


#print(f'You selected: {sections_to_retrieve}')


class AFD:
    """
    AFD class
    """
    def __init__(self, wfo, versions=45):
        self.wfo = wfo
        self.versions = min(int(versions), 50)
        self.section_dict = {}
        self.grab_bulletins()
        self.write_text()

    def get_time(self, line):
        """
        input:
            String: "Issued at" line (Ex: 'Issued at 307 AM EST Sat Dec 18 2021')
            return: datestring
             %I      7   Hour (12-hour clock) as a decimal number. (Platform specific)
             %M     06   Minute as a zero-padded decimal number.
             %p     AM   Locale’s equivalent of either AM or PM.
             %a    Sun   Weekday as locale’s abbreviated name.
             %b    Sep   Month as locale’s abbreviated name.
             %-d     8   Day of the month as a decimal number. (Platform specific)
             %Y   2013   Year with century as a decimal number.

        """
        # test = 'Issued at 1207 PM EST Sat Dec 8 2021'
        try:
            elements = line.split(" ")
            # remove the time zone and day of week because they don't matter
            extracted_elements = elements[2:4] + elements[6:]
            shortened_time_string = " ".join(extracted_elements)
            datetime_object = datetime.strptime(
                shortened_time_string, '%I%M %p %b %d %Y')
            new_datetime_string = datetime.strftime(
                datetime_object, '%Y%m%d%H%M')
        except ValueError:
            new_datetime_string = "ZZZZ_Missing"

        return new_datetime_string

    def get_forecaster_id(self, afd_text, section_name):
        """_summary_

        Args:
            afd_text (_type_): _description_
            section_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        buffer = '  --------------------------  '
        section_name_minus_leading_period = section_name[1:]
        forecaster_id_section = afd_text.split('$$')[-1]
        id_lines = forecaster_id_section.splitlines()
        fcstr = 'None found'
        for line in id_lines:
            if section_name_minus_leading_period in line:
                fcstr = str(line.split("...")[1])
                final = f'\n\n{buffer}{fcstr}{buffer}\n\n'
                break

        return final

    def get_section(self, afd_text, section_name):
        """_summary_

        Args:
            afd_text (_type_): _description_
            section_name (_type_): _description_
        """
        datetime_string = "ZZZZ_Missing"
        try:
            section_text = afd_text.split(section_name)[1]
        except IndexError:
            return

        #issuance_time_string = self.get_time(section_text)

        try:
            forecaster_id = self.get_forecaster_id(afd_text, section_name)
        except IndexError:
            print('forecaster id missing!')

        section_data = []
        for line in section_text.splitlines():
            if '&amp;&amp;' in line or '$' in line or '.LONG TERM' in line:
                break
            if 'Issued at' in line:
                datetime_string = self.get_time(line)
                section_data.append(line)
            else:
                section_data.append(line)

        section_content = '\n'.join(section_data)

        unique_section_identifier = f'{datetime_string}_{section_name}'
        final_section_text = f'{forecaster_id}{section_name}{section_content}'
        self.section_dict[unique_section_identifier] = final_section_text
        return

    def grab_bulletins(self):
        """_summary_
        """
        for version in range(1, self.versions):
            next_url = f'https://forecast.weather.gov/product.php?site={self.wfo}&issuedby={self.wfo}&product=AFD&format=ci&version={version}&glossary=0'
            next_page = requests.get(next_url, timeout=5)
            next_soup = BeautifulSoup(next_page.content, 'html.parser')
            afd_text = str(next_soup.pre)
            for section in sections_to_retrieve:
                self.get_section(afd_text, section)

    def write_text(self):
        """_summary_
        """
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as fout:
            for value in self.section_dict.values():
                fout.write(value)


if __name__ == '__main__':
    test = AFD("GRR", 45)
    