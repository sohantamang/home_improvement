import json
import requests
from datetime import datetime
response = requests.get('https://developer.trimet.org/ws/V1/arrivals?locIDs=9821&appID=appidhere&json=true')
response.content.decode("utf-8")
data = response.json()
print(data)
for arrival in data['resultSet']['arrival']:
    print(arrival['shortSign'] ,datetime.strptime(arrival['estimated'],"%Y-%m-%dT%H:%M:%S.000%z").strftime('%I:%M%p'))
