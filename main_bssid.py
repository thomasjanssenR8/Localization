"""
6-Bachelor thesis: Wi-Fi localization - Thomas Janssen
Localization v2: Use BSSID of a network to find coordinates via www.wigle.net and calculate the error.
"""

import requests
import numpy as np
import matplotlib.pyplot as plt
import haversine
import subprocess

# @TODO: Tel aantal request per 24 uur: 2


class Localization:
    userID = ""
    password = ""
    url = ""
    netid1 = ""
    netid2 = ""
    resultsPerPage = 1  # default=10 (daily limited amount of requests!)

    def __init__(self, userID, password, resultsPerPage):
        self.userID = userID
        self.password = password
        self.resultsPerPage = resultsPerPage

    def setuserID(self, newUserID):
        userID = newUserID
        print("User ID set to " + userID)

    def setPassword(self, newPassword):
        password = newPassword
        print("Password set to " + password)

    def setNetID(self, newNetID):
        netid = newNetID
        return netid

    def setResultsPerPage(self, newResultsPerPage):
        self.resultsPerPage = newResultsPerPage
        return self.resultsPerPage

    def getBSSIDs(self):
        cmd_output = subprocess.check_output('netsh wlan show networks mode=bssid')
        print(cmd_output)
        cmd = cmd_output.decode('UTF-8')
        index1 = cmd.find("BSSID")  # index of first letter that matches the string
        index2 = cmd.find("BSSID", index1 + 1)
        bssid1 = cmd[(index1 + 26):index1 + 43]  # 26-43 = BSSID (network MAC-adres)
        bssid2 = cmd[(index2 + 26):index2 + 43]
        print(bssid1)
        print(bssid2)
        bssids = [bssid1, bssid2]
        return bssids

    def createURLwithNetID(self, netid, resultsPerPage):
        url = "https://api.wigle.net/api/v2/network/search?freenet=false&paynet=false&netid=%s&resultsPerPage=%s" \
              % (netid, resultsPerPage)
        return url

    def request(self, url):
        r = requests.get(url, auth=('AID6e6e0f71da38f4b56d8c5990b0a540f1',  # Authentication:
                                    '848f760ac689e986a7f14120c014124d'))    # API name + API token from Wigle.net account ThomasJanssen
        print(r.text)  # print string
        return r

    def decodeObject(self, request):
        data = request.json()

        results = data['results']
        if not results:  # if list is empty
            coordinate = []
        else:
            trilat = results[0]['trilat']
            trilong = results[0]['trilong']
            print("Coordinate : N" + str(trilat) + " E" + str(trilong))
            coordinate = [trilat, trilong]

        return coordinate

    def calcMean(self, coord1, coord2):
        sum_latitudes = coord1[0] + coord2[0]
        sum_longitudes = coord1[1] + coord2[1]
        mean_latitude = sum_latitudes / 2  # evt. afronden: round(floatgetal, 8)
        mean_longitude = sum_longitudes / 2
        print("Mean coordinate: N" + str(mean_latitude) + " E" + str(mean_longitude))
        calcedMean = [mean_latitude, mean_longitude]
        return calcedMean

    def calcError(self, mean):
        measuredLatitude = float(input("Give the latitude of the coordinate you measured: "))
        measuredLongitude = float(input("Give the longitude of the coordinate you measured: "))
        # latitudeError = abs(measuredLatitude - mean[0])
        # longitudeError = abs(measuredLongitude - mean[1])
        # print("The coordinate error is " + str(latitudeError) + ", " + str(longitudeError))
        measurementCoordinate = (measuredLatitude, measuredLongitude)
        meanCoordinate = (mean[0], mean[1])
        distance = haversine.haversine(measurementCoordinate, meanCoordinate)
        print("The distance between the coordinates is " + str(distance) + " km")  # print difference in kilometers

    def plotCoordinates(self, coord1, coord2):
        plt.scatter(coord1[0], coord1[1])
        plt.scatter(coord2[0], coord2[1])
        plt.suptitle('Mean coordinate vs. Measured coordinate')
        plt.show()




# Authenticate, perform HTTP-request to Wigle-server, find coordinates in JSON-string, plot them and calculate mean
# -----------------------------------------------------------------------------------------------------------------
l = Localization("user", "pw", 1)                               # Create Localization object
l.resultsPerPage = 2                                            # with 2 netID's and 2 resultsPerPage
[l.netid1, l.netid2] = l.getBSSIDs()

url1 = l.createURLwithNetID(l.netid1, l.resultsPerPage)         # Create URL  with given BSSID (netid) 1
url2 = l.createURLwithNetID(l.netid2, l.resultsPerPage)         # Create URL  with given BSSID (netid) 2
print("Created URL 1:   " + url1)
print("Created URL 2:   " + url2)

request1 = l.request(url1)                                      # Perform 2 requests
request2 = l.request(url2)

coordinate1 = l.decodeObject(request1)                          # response unmarshalling (+ print data to console)
coordinate2 = l.decodeObject(request2)

if len(coordinate1) == 0 or len(coordinate2) == 0:
    print("One or two of the BSSID's were not found in the Wigle database.")
else:
    mean = l.calcMean(coordinate1, coordinate2)                 # calculate the mean position of the coordinates
    l.calcError(mean)                                           # calculate error between measured and real coordinate
    l.plotCoordinates(coordinate1, coordinate2)                 # plot coordinates in scatter plot








# Use this in case daily limit of requests is reached:
# -----------------------------------------------------------------------------------------------------------------
# param1 = data["success"]  # Use this in case daily limit of requests is reached
# param2 = data["error"]
# print(param1)
# print(param2)
# positions = [param1, param2]

#data = '{"resultCount":5,"last":5,"success":true,"results":[{"trilat":51.22378540,"trilong":4.40892172,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:18.000Z","lasttime":"2015-02-22T11:26:18.000Z","lastupdt":"2015-02-22T09:28:02.000Z","netid":"00:0B:86:26:79:C5","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22327042,"trilong":4.40893793,"ssid":"UAntwerpen","qos":4,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:32.000Z","lasttime":"2014-03-09T07:15:11.000Z","lastupdt":"2014-03-09T05:15:16.000Z","netid":"00:0B:86:26:7A:75","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22335815,"trilong":4.40887070,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:20.000Z","lasttime":"2016-04-24T13:59:46.000Z","lastupdt":"2016-04-24T14:00:33.000Z","netid":"00:0B:86:26:7E:75","name":null,"type":"infra","comment":null,"wep":"2","channel":11,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22303772,"trilong":4.40889168,"ssid":"UAntwerpen","qos":0,"transid":"20140304-00114","firsttime":"2014-03-04T21:48:51.000Z","lasttime":"2014-03-05T19:18:58.000Z","lastupdt":"2014-03-05T17:19:23.000Z","netid":"00:0B:86:26:7E:D5","name":null,"type":"infra","comment":null,"wep":"2","channel":1,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.17709351,"trilong":4.41607475,"ssid":"UAntwerpen","qos":1,"transid":"20110605-00081","firsttime":"2011-05-31T17:11:13.000Z","lasttime":"2013-10-28T11:32:52.000Z","lastupdt":"2013-10-28T09:33:29.000Z","netid":"00:0b:86:26:86:16","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false}],"first":1}'
# latitude_index = data.find("trilat") + 8
# latitude = data[latitude_index: (latitude_index+11)]
# print("N"+latitude)
#
# longitude_index = data.find("trilong") + 9
# longitude = data[longitude_index: (longitude_index+10)]
# print("E"+longitude)


# s.addCoordinate(51.22378540, 4.40892172)  # Coordinates from wigle request with ssid=Uantwerpen (stadscampus)
# s.addCoordinate(51.22327042, 4.40893793)
# s.addCoordinate(51.22335815, 4.40887070)
# s.addCoordinate(51.22303772, 4.40889168)
# s.addCoordinate(51.17709351, 4.41607475)  # Campus Groenenborger
# s.plotScatter()

# Show BSSID's in Windows cmd: netsh wlan show networks mode=bssid












