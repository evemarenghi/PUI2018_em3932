from __future__ import print_function

import requests
import os 
import json
import sys 
from urllib.request import Request, urlopen

# syntax that allows you to bypass calls that would cause an error 
# we need to write code that works in both python 2 and python 3
# an if statement would cause the program to crash 
# try and except works without causing the program to crash 

# except ImportError --> tell us exactly which error to look for 
# every error that has an error code that must be included in the except statement 
# if you just use 'except', you will get an error but you won't know what caused it 
try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib  
    
# debug flag
DEBUG = False # You can add lines that you only want to run in debug mode, e.g. print statements 

# doc string --> when you have a function and you don't know what it does 
# add doc strings for your functions so people can find out what they do 
# there is a specific format for doc strings --> 3 quotes 


# we need to collect arguments as input from the user 
# check if the number of arguments passed to the string is correct 
# provide the user with feedback 
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Please enter script name, API key, bus line, and name of output file.")
    sys.exit()
    
# key, bus_line, outfile = sys.arv[1:]  --> more compact way to assign the input variables 
# of = open(outfile, 'w')

key = str(sys.argv[1])
bus_line = str(sys.argv[2])
output_file = open(sys.argv[3], "w")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

pass_url = url + key + url2 + bus_line

# Debug mode --> print statements to check if the code is working correctly 
# if DEBUG:
#    print('#BUS LINE:', bus_line)

# Gives you visibility into the code so that you can see what's going on 
# if DEBUG: 
#    print("URL of the bus", bus_url)

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