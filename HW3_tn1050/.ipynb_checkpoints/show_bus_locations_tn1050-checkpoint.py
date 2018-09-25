import pylab as pl
import pprint
import os
import json
import sys
import pandas as pd
import pprint
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apiKey='81e3ec91-9d70-49cf-8a2a-d5a0adec6c21'#sys.argv[1]
busLine='B52'#sys.argv[2]

print('Key=%s' % apiKey)
print('Bus Line=%s' % busLine)
print('Fetching URL...')
url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (apiKey, busLine)
print(url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

df=pd.DataFrame(columns=['latitude', 'longitude'])
k=0
for i in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    i=i['MonitoredVehicleJourney']
    vehicleLocation=i['VehicleLocation']
    row1=[vehicleLocation['Latitude'],vehicleLocation['Latitude']]
    pprint.pprint(i)
    df.loc[k]=row1
    k+=1
    break