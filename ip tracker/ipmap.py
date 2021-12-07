import os 
import urllib.request as ur
import json

while True:
    def i():

      ip=input("What is your target IP: ")
      url= "http://ip-api.com/json/" 
      response = ur.urlopen(url + ip)
      data =response.read() 
      values= json.loads(data)
      print(" IP: " + values['query'])
      print(" City: "+ values['city']) 
      print(" ISP(internet service provider): " + values['isp'])
      print ("Country: "+ values [ 'country']) 
      print("Region: "+ values ['region']) 
      print("Time zone:" + values[ 'timezone'])
    break 
i()
#122.187.108.170