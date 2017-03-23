"""
6-Bachelor thesis: Wi-Fi localization - Thomas Janssen
Localization v2: Use BSSID of a network to find coordinates via www.wigle.net and calculate the error.
"""

import requests
import openpyxl


def getBSSIDs():
    bssids = []
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=1, max_col=1):
        for cell in row:
            bssids.append(cell.value)
    return bssids


def createURLwithNetID(netid):
    url = "https://api.wigle.net/api/v2/network/search?freenet=false&paynet=false&netid=%s&resultsPerPage=1" % netid
    return url


def request(url):
    r = requests.get(url, auth=('AID6e6e0f71da38f4b56d8c5990b0a540f1',  # Authentication:
                                '848f760ac689e986a7f14120c014124d'))    # API name + API token from Wigle.net account ThomasJanssen
    print(r.text)  # print string
    return r


def decodeObject(request):
    data = request.json()
    if not data['success'] or not data['results']:                                      # If daily limit reached or empty list
        coordinate = []
        print('Succes = false')
    else:
        results = data['results']
        trilat = results[0]['trilat']
        trilong = results[0]['trilong']
        print("Coordinate : N" + str(trilat) + " E" + str(trilong))
        coordinate = [trilat, trilong]
    return coordinate


# def calcMean(coord1, coord2):
#     sum_latitudes = coord1[0] + coord2[0]
#     sum_longitudes = coord1[1] + coord2[1]
#     mean_latitude = sum_latitudes / 2  # evt. afronden: round(floatgetal, 8)
#     mean_longitude = sum_longitudes / 2
#     print("Mean coordinate: N" + str(mean_latitude) + " E" + str(mean_longitude))
#     calcedMean = [mean_latitude, mean_longitude]
#     return calcedMean
#
#
# def calcError(mean):
#     measuredLatitude = float(input("Give the latitude of the coordinate you measured: "))
#     measuredLongitude = float(input("Give the longitude of the coordinate you measured: "))
#     # latitudeError = abs(measuredLatitude - mean[0])
#     # longitudeError = abs(measuredLongitude - mean[1])
#     # print("The coordinate error is " + str(latitudeError) + ", " + str(longitudeError))
#     measurementCoordinate = (measuredLatitude, measuredLongitude)
#     meanCoordinate = (mean[0], mean[1])
#     distance = haversine.haversine(measurementCoordinate, meanCoordinate)
#     print("The distance between the coordinates is " + str(distance) + " km")  # print difference in kilometers
#     measurement = [measuredLatitude, measuredLongitude, distance]
#     return measurement
#
#
# def plotCoordinates(coord1, coord2):
#     plt.scatter(coord1[0], coord1[1])
#     plt.scatter(coord2[0], coord2[1])
#     plt.suptitle('Mean coordinate vs. Measured coordinate')
#     plt.show()



#  Main program
# -----------------------------------------------------------------------------------------------------------------
file = 'bssids.xlsx'                                    # Load Excel sheet
book = openpyxl.load_workbook(filename=file)
sheet = book.active
start_row = int(input('Give the starting row index: '))
end_row = int(input('Give the ending row index: '))

bssids = getBSSIDs()                                    # Get the BSSIDs in the vicinity using CMD
count = 0
rowindex = start_row

for bssid in bssids:                                    # Iterate over every BSSID
    url = createURLwithNetID(bssid)                     # Create URL  with given BSSID (netid)
    print("Created URL:   " + url)
    req = request(url)                                  # Perform request
    coordinate = decodeObject(req)                      # Unmarshalling: find coordinates in json string and print
    if len(coordinate) == 0:
        print("BSSID not found in the Wigle database or daily limit reached.")
    else:                                               # Write coordinate to excel
        Eindex = 'E' + str(rowindex)
        Findex = 'F' + str(rowindex)
        sheet[Eindex] = float(coordinate[0])            # Latitude
        sheet[Findex] = float(coordinate[1])            # Longitude
    count += 1
    rowindex += 1
    book.save(file)

# -------------------------------------------------------------------------------------------------------------------




# mean = calcMean(allcoordinates)                               # Calculate the mean position of the coordinates
# measure = calcError(mean)                                     # Calculate error between measured and real coordinate
# plotCoordinates(allcoordinates)                               # Plot coordinates in scatter plot
# writeToFile(mean, measure)                                    # Write results to xlsx file
















