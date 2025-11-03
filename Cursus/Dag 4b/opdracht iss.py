import time

import requests
import plotly.express as px

def get_iss_position():
    url = 'https://api.wheretheiss.at/v1/satellites/25544'

    r = requests.get(url)

    if r.status_code != 200:
        print('Error', r.status_code)
        exit()

    d = r.json()

    lat = d['latitude']
    lon = d['longitude']

    return lat, lon


def get_geo_location(lat, lon):
    apikey = 'd1526a9039658a6f76950cff21823aff'

    url = 'http://api.openweathermap.org/geo/1.0/reverse'
    url += f'?appid={apikey}'
    url += f'&lat={lat}'
    url += f'&lon={lon}'
    url += '&limit=10'

    # print(url)

    r = requests.get(url)

    if r.status_code != 200:
        print('Error', r.status_code)
        exit()

    d = r.json()

    if d == []:
        return '?'

    return d[0]['country'], d[0]['state'], d[0]['name']


# lat, lon = 52, 5.25
# country = get_geo_location(lat, lon)
# print(f'{lat}, {lon} => {country}')


while True:
    try:
        lat, lon = get_iss_position()
        location = get_geo_location(lat, lon)
        print(f'{lat}, {lon} => {location}')
        time.sleep(5)

    except KeyboardInterrupt:
        print('OK. Stopping ...')
        break