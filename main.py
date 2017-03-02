import requests

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

    def getResponse(self, url):
        response = requests.post(url, data=data)

    def request(self, url):
        r = requests.get(url, auth=('AID6e6e0f71da38f4b56d8c5990b0a540f1',  # Authentication:
                                    '848f760ac689e986a7f14120c014124d'))    # API name + API token from Wigle.net account ThomasJanssen
        print(r.text)  # print string
        return r

    def decodeObject(self, r):
        data = r.json()
        param1 = data["success"]
        param2 = data["error"]
        print(param1)
        print(param2)
        position = [param1, param2]

        # resultCount = data["resultCount"]
        # print("ResultCount = " + str(resultCount))
        # results = data["results"]
        # trilat = results[0]["trilat"]
        # print("Latitude = " + str(trilat))
        # trilong = results[0]["trilong"]
        # print("Longitude = " + str(trilong))
        # position = [trilat, trilong]

        return position



l = Localization("user", "pw")

input_resultsPerPage = input("Give amount of results per page: ")
input_ssid = input("Give the SSID you are looking for: ")

url = l.createURL(input_ssid, input_resultsPerPage)
print(url)

request = l.request(url)            # perform the request
position = l.decodeObject(request)  # response unmarshalling (this function also prints the data to the output)



# Temporary data (daily limited amount of requests!)
data = '{"resultCount":1,"last":1,"success":true,"results":[{"trilat":51.22378540,"trilong":4.40892172,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:18.000Z","lasttime":"2015-02-22T11:26:18.000Z","lastupdt":"2015-02-22T09:28:02.000Z","netid":"00:0B:86:26:79:C5","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false}],"first":1}'

latitude_index = data.find("trilat") + 8
latitude = data[latitude_index: (latitude_index+11)]
print("N"+latitude)

longitude_index = data.find("trilong") + 9
longitude = data[longitude_index: (longitude_index+10)]
print("E"+longitude)


# import scatter
# s = scatter()
# s.addCoordinate(51.22378540, 4.40892172)  # Coordinates from wigle request with ssid=Uantwerpen (stadscampus)
# s.addCoordinate(51.22327042, 4.40893793)
# s.addCoordinate(51.22335815, 4.40887070)
# s.addCoordinate(51.22303772, 4.40889168)
# s.addCoordinate(51.17709351, 4.41607475)  # Campus Groenenborger
# s.plotScatter()
















