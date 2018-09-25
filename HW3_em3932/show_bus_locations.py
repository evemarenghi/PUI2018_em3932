from __future__ import print_function

import requests
import os 
import json
import sys 
from urllib.request import Request, urlopen

try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib  

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Please enter script name, API key, and bus line.")
    sys.exit()
    
api_key = str(sys.argv[1])
bus_line = str(sys.argv[2])
    
print("Bus Line : " + bus_line)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

pass_url = url + api_key + url2 + bus_line

response = urllib.urlopen(pass_url)
data = response.read().decode('utf-8')
data = json.loads(data)

bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Number of Active Buses : " + str(len(bus_data)))

bus_number = 0 
for i in bus_data:
    print("Bus " + str(bus_number) + " is at latitude " + str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
         + " and longitude " + str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    bus_number += 1