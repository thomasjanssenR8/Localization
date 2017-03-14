# from urllib import urlopen
# from pylab import imshow, imread, show
#
# lon = [49.5, 50.35]
# lat = [18.6, 20.2]
# scale = 700000
#
# # open an openstreetmap export png file via http
# url = urlopen('http://parent.tile.openstreetmap.org/cgi-bin/export?'
#               'bbox={lat1:.2f},{lon1:.2f},{lat2:.2f},{lon2:.2f}&'
#               'scale={scale:d}&format=png'.format(lat1=lat[0],
#               lat2=lat[1],
#               lon1=lon[0],
#               lon2=lon[1],
#               scale=scale))
#
# # plot the map
# imshow(imread(url), extent=lat+lon, aspect='equal')
#
# # plot other data here
#
# show()


import haversine
mean = [51.123456, 4.58541]

measuredLatitude = float(input("Give the latitude of the coordinate you measured: "))
measuredLongitude = float(input("Give the longitude of the coordinate you measured: "))
latitudeError = abs(measuredLatitude - mean[0])
longitudeError = abs(measuredLongitude - mean[1])
print("The coordinate error is " + str(latitudeError) + ", " + str(longitudeError))

measurementCoordinate = (measuredLatitude, measuredLongitude)
meanCoordinate = (mean[0], mean[1])
distance = haversine.haversine(measurementCoordinate, meanCoordinate)
print("The distance between the coordinates is " + str(distance) + " km")  # print difference in kilometers

