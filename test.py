import haversine


def calcError(mean):
    measuredLatitude = float(input("Give the latitude of the coordinate you measured: "))
    measuredLongitude = float(input("Give the longitude of the coordinate you measured: "))
    measurementCoordinate = (measuredLatitude, measuredLongitude)
    meanCoordinate = (mean[0], mean[1])
    distance = haversine.haversine(measurementCoordinate, meanCoordinate)
    print("The distance between the coordinates is " + str(distance) + " km")  # print difference in kilometers


calcError([51.22286987, 4.41602373])



