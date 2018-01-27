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


# list of sources
sources = [
    'https://api.ipify.org/?format=json',
    'http://ip-api.com/json',
    'http://ip.jsontest.com/',
    'https://ident.me/.json',
    'http://bot.whatismyipaddress.com/'
    'https://ifconfig.co/json'
    'https://wtfismyip.com/json'
]

responses = []

#walk through every source, save results to reponses

responses.append(datetime.datetime.now())

for source in sources:
    try:
        with urllib.request.urlopen(source) as response:
            try:
                data = json.loads(response.read().decode())
            except Exception as E:
                data = response.read().decode()

            print(data)
            responses.append(data)
    except:
        something

    sleep(5)

pickle_out = open("ipInfo.txt","wb")
pickle.dump(responses,pickle_out)
pickle_out.close()