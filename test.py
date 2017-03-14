import haversine

measurementCoordinate = (45.7597, 4.8422)
meanCoordinate = (48.8567, 2.3508)
print(haversine.haversine(measurementCoordinate, meanCoordinate))  # print difference in kilometers