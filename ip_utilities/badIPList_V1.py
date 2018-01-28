# This is the wrong way to make a 'Threat Intelligence' IP list, but from what I can tell, many products do exactly this.

from random import randint
from time import sleep
import ipaddress
import urllib.request
import json
import numpy as np

count = 0

class threatNugget:

    def __init__(self, address, type):

        self.ip = address
        self.type = ""
        self.source = ""
        self.severity = randint(1,10)
        self.confidence = randint(1,10)
        self.score = self.severity * self.confidence
        self.category = ""
        self.enhanced = "no"
        self.country = ""
        self.countryCode = ""
        self.region = ""
        self.regionName = ""
        self.city = ""
        self.zip = ""
        self.lat = ""
        self.lon = ""
        self.timezone = ""
        self.isp = ""
        self.asn = ""

    def __repr__(self):

        attribs = vars(self)

        return (', '.join("%s: %s" % item for item in attribs.items()))

def buildList(quantity):
    foundIndicators = []

    type = "v4"

    for i in range(0, quantity):
        foundIndicators.append(threatNugget(ipaddress.IPv4Address(randint(1, 0xffffffff)),type))

    #feature available to "enhanced users" only
    #type = "v6"

    #for i in range(0, quantity):
    #    foundIndicators.append(threatNugget(ipaddress.IPv6Address(randint(1, 0xffffffffffffffffffffffffffffffff)),type))

#    for nugget in foundIndicators:
#        print(nugget)

    return foundIndicators

def enhanceNuggets(uninhancedNuggets):

    results = []

    for each in uninhancedNuggets:
        try:
            sleep(1)
            print("Fetching info on " + str(each.ip))
            with urllib.request.urlopen("http://ip-api.com/json" + "/" + str(each.ip)) as response:
                try:
                    data = json.loads(response.read().decode())
                    #pass json data into threatNugget

                    if data["status"] != 'success':
                        print("There was an error with the IP provided:")
                        print(data["message"])

                    else:
                        each.enhanced = data["status"]
                        each.country = data["country"]
                        each.countryCode = data["countryCode"]
                        each.region = data["region"]
                        each.regionName = data["regionName"]
                        each.city = data["city"]
                        each.zip = data["zip"]
                        each.lat = data["lat"]
                        each.lon = data["lon"]
                        each.timezone = data["timezone"]
                        each.isp = data["isp"]
                        each.asn = data["as"]

                        print("Found info on: " + str(each.ip) + ", Country Code = " + each.countryCode)

                        #add enhanced nugget to list
                        results.append(each)

                except Exception as E:
                    print("There was an error parsing response\n" + str(E))
        except Exception as E:
            print("There was an error making the request\n" + str(E))

    return results

def saveNuggets(refinedNuggets):

    # this function has been a nightmare, I'm open to thoughts on how to get this output
    for nugget in refinedNuggets:
        printValue = (str(nugget.ip) + "," +
                      str(nugget.type) + "," +
                      str(nugget.score) + "," +
                      str(nugget.source) + "," +
                      str(nugget.severity) + "," +
                      str(nugget.confidence) + "," +
                      str(nugget.category) + "," +
                      str(nugget.enhanced) + "," +
                      str(nugget.country) + "," +
                      str(nugget.countryCode) + "," +
                      str(nugget.region) + "," +
                      str(nugget.regionName) + "," +
                      str(nugget.city) + "," +
                      str(nugget.zip) + "," +
                      str(nugget.lat) + "," +
                      str(nugget.lon) + "," +
                      str(nugget.timezone) + "," +
                      str(nugget.isp) + "," +
                      str(nugget.asn))

        print(printValue)
        with open('threatNuggets.csv','a', encoding='utf8') as resultsFile:
            resultsFile.write(printValue + '\n')


def main():

    rawNuggets = buildList(int(input("How many IPs do you want to investigate?")))

    refinedNuggets = enhanceNuggets(rawNuggets)

    refinedNuggets = sorted(refinedNuggets, key=lambda x: x.ip, reverse=True)

    saveNuggets(refinedNuggets)

main()