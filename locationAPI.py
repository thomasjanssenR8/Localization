from itertools import combinations
import openpyxl
import unwiredlabs


def get_data():
    start_row = end_row = 4                                     # Get starting and ending row
    stop = False
    while not stop:
        if not sheet.cell(row=end_row, column=1).value:
            stop = True
        else:
            end_row += 1
    end_row -= 1

    amount_of_bssids = end_row - start_row + 1                  # Count amount of BSSIDs
    print('Amount of BSSIDs: ' + str(amount_of_bssids))

    bssids = []                                                 # Get BSSIDs and RSSIs
    rssis = []
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=1, max_col=1):
        for cell in row:
            bssids.append(cell.value)
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=2, max_col=2):
        for cell in row:
            percentage = cell.value
            if percentage <= 0:                                 # Convert signal strength percentage to dBm
                dbm = -100
            elif percentage >= 100:
                dbm = -50
            else:
                dbm = (percentage / 2) - 100
            rssis.append(dbm)

    print(bssids)
    print(rssis)
    data = [bssids, rssis, start_row, end_row, amount_of_bssids]
    return data


def write_combinations_to_file():

    # Write amount of BSSIDS and combinations under the first table
    sheet.cell(row=end_row + 2, column=4).value = amount_of_bssids
    sheet.cell(row=end_row + 3, column=4).value = len(bssid_combs)

    row_index = end_row + 9

    # Write combination number in column A
    for i in range(0, len(bssid_combs)):
        sheet.cell(row=row_index + i, column=1).value = i + 1

    # Write BSSID 1 in column B
    for i in range(0, len(bssid_combs)):
        sheet.cell(row=row_index + i, column=2).value = bssid_combs[i][0]

    # Write RSSI 1 in column C
    for i in range(0, len(bssid_combs)):
        sheet.cell(row=row_index + i, column=3).value = rssi_combs[i][0]

    # Write BSSID 2 in column D
    for i in range(0, len(bssid_combs)):
        sheet.cell(row=row_index + i, column=4).value = bssid_combs[i][1]

    # Write RSSI 2 in column E
    for i in range(0, len(bssid_combs)):
        sheet.cell(row=row_index + i, column=5).value = rssi_combs[i][1]


def perform_request(bssid1, bssid2, rssi1, rssi2):
    request = unwiredlabs.UnwiredRequest()
    request.addAccessPoint(bssid1, rssi1)
    request.addAccessPoint(bssid2, rssi2)
    connection = unwiredlabs.UnwiredConnection(key='99c1d8b93a7f37')  # API key of account 'Thomas Janssen'
    response = connection.performRequest(request)

    if response.status != 'Ok':
            print('Error:', response.status)
    else:
            print('Response: ', response.coordinate)


#  Main program
#  --------------------------------------------------------------------------------------------------------------------
file = 'data_locationAPI.xlsx'                                  # Load Excel sheet of a location (e.g. BAP1)
book = openpyxl.load_workbook(filename=file)

for location in range(1, 2):                                   # Load a template sheet for all 36 locations
    sheet = book.get_sheet_by_name('BAP' + str(location))

    [bssids, rssis, start_row, end_row, amount_of_bssids] = get_data()  # retrieve requested data

    bssid_combs = list(combinations(bssids, 2))                 # Get all possible combinations of 2 BSSIDs
    rssi_combs = list(combinations(rssis, 2))                   # Get all the combinations of the 2 RSSIs (in dBm)

    write_combinations_to_file()                                # Write all possible combinations to Excel file

    # mean_latitudes = []
    # mean_longitudes = []
    #
    # calc_mean()                                                 # Calculate the mean coordinate of each pair of BSSIDs
    # calc_error()                                                # Calculate distance between GPS and mean coordinate
    # calc_chances()                                              # Calculate the chance a BSSID is not found in database
    # show_map()                                                  # Save heatmap of requested coordinates

    book.save(file)                                             # Save the data
    print('Sheet and map saved: BAP' + str(location) + '\n')

# ---------------------------------------------------------------------------------------------------------------------

# [bssid1, bssid2, rssi1, rssi2] = get_data()
# perform_request(bssid1, bssid2, rssi1, rssi2)
