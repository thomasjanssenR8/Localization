import requests

# @TODO: Tel aantal request per 24 uur: 3


class Localization:
    userID = ""
    password = ""
    url = ""
    ssid = ""
    resultsPerPage = 10  # default=10 (daily limited amount of requests!)

    def __init__(self, userID, password):
        self.userID = userID
        self.password = password

    def setuserID(self, newUserID):
        userID = newUserID
        print("User ID set to " + userID)

    def setPassword(self, newPassword):
        password = newPassword
        print("Password set to " + password)

    def setSSID(self, newSSID):
        ssid = newSSID
        return ssid

    def setResultsPerPage(self, newResultsPerPage):
        self.resultsPerPage = newResultsPerPage
        return self.resultsPerPage

    def createURL(self, ssid, resultsPerPage):
        url = "https://api.wigle.net/api/v2/network/search?freenet=false&paynet=false&ssid=%s&resultsPerPage=%s" \
              % (ssid, resultsPerPage)
        return url

    # def getResponse(self, url):
    #     response = requests.post(url, data=data)

    def request(self, url):
        r = requests.get(url, auth=('AID6e6e0f71da38f4b56d8c5990b0a540f1',  # Authentication:
                                    '848f760ac689e986a7f14120c014124d'))    # API name + API token from Wigle.net account ThomasJanssen
        print(r.text)  # print string
        return r

    def decodeObject(self, r):
        data = r.json()

        resultCount = data['resultCount']
        print("ResultCount = " + str(resultCount))

        results = data['results']

        count = 0
        positions = []

        for result in range(0, len(results)):
            trilat = results[count]['trilat']
            trilong = results[count]['trilong']
            print("Latitude = " + str(trilat) + ", Longitude = " + str(trilong))
            position = [trilat, trilong]
            positions.append(position)
            count += 1

        # param1 = data["success"]  # Use this in case daily limit of requests is reached
        # param2 = data["error"]
        # print(param1)
        # print(param2)
        # positions = [param1, param2]

        return positions


# Authenticate with username + password, perform HTTP-request tot Wigle-server, and find coordinates in JSON-string
# -----------------------------------------------------------------------------------------------------------------
l = Localization("user", "pw")

l.resultsPerPage = input("Give amount of results per page: ")
l.ssid = input("Give the SSID you are looking for: ")
url = l.createURL(l.ssid, l.resultsPerPage)
print("Created URL:   " + url)

request = l.request(url)            # perform the request
position = l.decodeObject(request)  # response unmarshalling (this function also prints the data to the output)



# Use this in case daily limit of requests is reached:
#data = '{"resultCount":5,"last":5,"success":true,"results":[{"trilat":51.22378540,"trilong":4.40892172,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:18.000Z","lasttime":"2015-02-22T11:26:18.000Z","lastupdt":"2015-02-22T09:28:02.000Z","netid":"00:0B:86:26:79:C5","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22327042,"trilong":4.40893793,"ssid":"UAntwerpen","qos":4,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:32.000Z","lasttime":"2014-03-09T07:15:11.000Z","lastupdt":"2014-03-09T05:15:16.000Z","netid":"00:0B:86:26:7A:75","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22335815,"trilong":4.40887070,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:20.000Z","lasttime":"2016-04-24T13:59:46.000Z","lastupdt":"2016-04-24T14:00:33.000Z","netid":"00:0B:86:26:7E:75","name":null,"type":"infra","comment":null,"wep":"2","channel":11,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.22303772,"trilong":4.40889168,"ssid":"UAntwerpen","qos":0,"transid":"20140304-00114","firsttime":"2014-03-04T21:48:51.000Z","lasttime":"2014-03-05T19:18:58.000Z","lastupdt":"2014-03-05T17:19:23.000Z","netid":"00:0B:86:26:7E:D5","name":null,"type":"infra","comment":null,"wep":"2","channel":1,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false},{"trilat":51.17709351,"trilong":4.41607475,"ssid":"UAntwerpen","qos":1,"transid":"20110605-00081","firsttime":"2011-05-31T17:11:13.000Z","lasttime":"2013-10-28T11:32:52.000Z","lastupdt":"2013-10-28T09:33:29.000Z","netid":"00:0b:86:26:86:16","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false}],"first":1}'
# latitude_index = data.find("trilat") + 8
# latitude = data[latitude_index: (latitude_index+11)]
# print("N"+latitude)
#
# longitude_index = data.find("trilong") + 9
# longitude = data[longitude_index: (longitude_index+10)]
# print("E"+longitude)


# import scatter:
# s = Scatter()
# s.addCoordinate(51.22378540, 4.40892172)  # Coordinates from wigle request with ssid=Uantwerpen (stadscampus)
# s.addCoordinate(51.22327042, 4.40893793)
# s.addCoordinate(51.22335815, 4.40887070)
# s.addCoordinate(51.22303772, 4.40889168)
# s.addCoordinate(51.17709351, 4.41607475)  # Campus Groenenborger
# s.plotScatter()

















