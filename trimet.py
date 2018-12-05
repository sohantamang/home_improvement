import json
import requests
from datetime import datetime, timezone, timedelta
import yaml
import time, threading


def set_arrival(config, stopid):
    return config['HOME_URL'] + '/ws/V1/arrivals?locIDs='\
        + stopid + '&appID=' + config['APP_ID'] + '&json=true'

def show_arrivals(url):
    response = requests.get(url)
    data = response.json()
    data['resultSet']
    for arrival in data['resultSet']['arrival']:
        estimated_time = datetime.strptime(arrival.get('estimated', arrival['scheduled']),"%Y-%m-%dT%H:%M:%S.%f%z")
        current_time = datetime.now(timezone(timedelta(hours=-8)))
        remaining_minutes = int((estimated_time - current_time).seconds/60)
        print(arrival['shortSign'] ,estimated_time.strftime('%I:%M%p'),remaining_minutes, 'minutes'  )
    print('')
    threading.Timer(40, lambda: show_arrivals(url)).start()

config = yaml.load(open('configs/config.yml'))
url = set_arrival(config, config['BTC'])
show_arrivals(url)
