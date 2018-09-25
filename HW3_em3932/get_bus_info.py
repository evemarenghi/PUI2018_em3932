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

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Please enter script name, API key, bus line, and name of output file.")
    sys.exit()

key = str(sys.argv[1])
bus_line = str(sys.argv[2])
output_file = open(sys.argv[3], "w")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

pass_url = url + key + url2 + bus_line

response = urllib.urlopen(pass_url)
data = response.read().decode('utf-8')
data = json.loads(data)

bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

output_file.write("Latitude,Longitude,Stop Name, Stop Status\n")

bus_number = 0 
for i in bus_data:
    lat = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    lon = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']) 
    if i['MonitoredVehicleJourney']['OnwardCalls']:
        stop_name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    else:
        stop_name = "N/A"
    if i['MonitoredVehicleJourney']['OnwardCalls']:
        stop_status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    else:
        stop_status = "N/A"
    output_file.write("%s," % lat)
    output_file.write("%s," % lon)
    output_file.write("%s," % stop_name)
    output_file.write("%s\n" % stop_status)
    bus_number += 1

output_file.close()