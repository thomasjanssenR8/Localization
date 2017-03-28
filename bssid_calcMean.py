import openpyxl
from itertools import combinations


def getCoordinates():
    latitudes = []
    longitudes = []
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=5, max_col=5):
        for cell in row:
            latitudes.append(cell.value)
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=6, max_col=6):
        for cell in row:
            longitudes.append(cell.value)
    coordinates = [latitudes, longitudes]
    return coordinates


file = 'bssids.xlsx'                                            # Load Excel sheet
book = openpyxl.load_workbook(filename=file)
sheet = book.active
start_row = int(input('Give the starting row index: '))
end_row = int(input('Give the ending row index: '))

[lat, long] = getCoordinates()                                  # Print all the combinations of the measured coordinates
latCombs = list(combinations(lat, 2))
longCombs = list(combinations(long, 2))
print(latCombs)
print(longCombs)




