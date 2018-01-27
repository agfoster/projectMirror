import urllib.request
import json
import pickle
import datetime
from time import sleep
import os

#setup
homeDir = os.path.expanduser('~')
os.chdir(homeDir)
if not os.path.exists('pyInvestigator'):
    os.makedirs('pyInvestigator')
os.chdir('pyInvestigator')
    #run setup script
    #print('Run setup script')

pickle_in = open("ipInfo.txt","rb")
responses = pickle.load(pickle_in)
pickle_in.close()

#for response in responses:
#    print(str(type(response)) + ":" + str(response))

print("The following information was collected on: " + str(responses[0]))

#count the number of unique IP addresses
ipResults = []

for response in responses:
    print(response)

for response in responses:
   if type(response) == dict:
       try:
           ipResults.append(response['YourFuckingIPAddress'])
       except:
           pass
       try:
           ipResults.append(response['ip'])
       except:
           pass
       try:
           ipResults.append(response['address'])
       except:
           pass
       try:
           ipResults.append(response['query'])
       except:
           pass

print(ipResults)