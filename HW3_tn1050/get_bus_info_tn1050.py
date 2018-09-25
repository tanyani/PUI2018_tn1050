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
busLine=str(sys.argv[2])
output=str(sys.argv[3])
url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (apiKey, busLine)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
allBus=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

df=pd.DataFrame(columns=['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
k=0
find=['approaching', '1 stop away']
print (len(allBus))
for i in allBus:
    i=i['MonitoredVehicleJourney']
    vehicleLocation=i['VehicleLocation']
    onwardCalls=i['OnwardCalls']
    if len(onwardCalls)<1:
        row=[vehicleLocation['Latitude'], vehicleLocation['Longitude'], 'N/A', 'N/A']
    else:
        onwardCall=onwardCalls['OnwardCall']
        for j in onwardCall:
            presDist=j['Extensions']['Distances']['PresentableDistance']
            stopName=j['StopPointName']
            if(presDist in find):
                row=[vehicleLocation['Latitude'], vehicleLocation['Longitude'], stopName, presDist]
                break
            else:
                row=[vehicleLocation['Latitude'], vehicleLocation['Longitude'], 'N/A', 'N/A']
        df.loc[k]=row
    k+=1
print(output)
df.to_csv(output, index=False)
