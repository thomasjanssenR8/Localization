"""
Draw a scatter plot with the data obtained by the http request, based on latitude and longitude.
"""
import numpy as np
import matplotlib.pyplot as plt


class Coordinate:
    latitude = ""
    longitude = ""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def setCoordinate(self, newLatitude, newLongitude):
        self.latitude = newLatitude
        self.longitude = newLongitude

    def printCoordinate(self):
        print("Coordinate: latitude = " + str(self.latitude) + ", longitude = " + str(self.longitude))


class Scatter:
    coordinates = []

    def addCoordinate(self, altitude, longitude):
        c = Coordinate(altitude, longitude)
        self.coordinates.append(c)

    def plotScatter(self):
        for coordinate in self.coordinates:
            coordinate.printCoordinate()
            plt.scatter(coordinate.latitude, coordinate.longitude)

        # plt.xlim(50, 60)
        # plt.ylim(0, 5)
        plt.suptitle('Scatter plot of some coordinates')
        plt.show()


# Zet dit in main.py
s = Scatter()
s.addCoordinate(51.22378540, 4.40892172)  # Coordinates from wigle http-request with ssid=Uantwerpen (stadscampus)
s.addCoordinate(51.22327042, 4.40893793)
s.addCoordinate(51.22335815, 4.40887070)
s.addCoordinate(51.22303772, 4.40889168)
s.addCoordinate(51.17709351, 4.41607475)  # Campus Groenenborger
s.plotScatter()


# Latitude goes from -90 to 90 , longitude goes from -180 to 180









