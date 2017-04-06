import gmplot

latitudes = [51, 51.1, 51.23]
longitudes = [4, 4.4, 4.6]

gmap = gmplot.GoogleMapPlotter(51.215250, 4.411549, 16)

# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
gmap.heatmap(latitudes, longitudes)

gmap.draw("mymap.html")

