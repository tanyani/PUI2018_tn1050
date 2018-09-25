import pylab as pl
import pprint
import os
import json
import sys
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apiKey=sys.argv[1]
busLine=sys.argv[2]
url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (apiKey, busLine)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
allBus=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

k=0
print('Bus Line : %s' % busLine)
print('Number of active buses : %s' % (len(allBus)))
for i in allBus:
    i=i['MonitoredVehicleJourney']
    vehicleLocation=i['VehicleLocation']
    print('Bus %s is at latitude %s and longitude %s' % (k, vehicleLocation['Latitude'], vehicleLocation['Longitude']))
    k+=1
