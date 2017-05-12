import openpyxl


def get_data():
    start_row = end_row = 4                                 # Get starting row of BSSIDs
    stop = False
    while not stop:                                         # Get ending row of BSSIDs
        if not sheet.cell(row=end_row, column=1).value:
            stop = True
        else:
            end_row += 1
    end_row -= 1

    amount_of_bssids = end_row - start_row + 1
    print('Amount of BSSIDs: ', amount_of_bssids)
    amount_of_bssid_combs = sheet.cell(row=end_row+3, column=3).value  # Get amount of possible combinations of 2 BSSIDs
    print('Amount of combinations: ', amount_of_bssid_combs)

    begin_combs = end_row + 6
    end_combs = begin_combs + amount_of_bssid_combs - 1
    errors = []
    rssis = []

    for j in range(start_row, end_row+1):                           # Load RSSI values
        rssis.append(sheet.cell(row=j, column=2).value)

    for i in range(begin_combs, end_combs+1):
        if sheet.cell(row=i, column=7).value:
            errors.append(sheet.cell(row=i, column=10).value)       # Load distance errors (without None)
    read_data = [start_row, end_row, rssis, begin_combs, end_combs, errors]
    return read_data


book_read = openpyxl.load_workbook(filename='data\\data_wigle.xlsx')  # Load Excel sheets
book_write = openpyxl.load_workbook(filename='data\\data_comparison.xlsx')
sheet_write = book_write.get_sheet_by_name('Highest RSSI')

for location in range(1, 2):                                       # Load a template sheet for all 36 locations
    sheet = book_read.get_sheet_by_name('BAP' + str(location))

    [start_row, end_row, rssis, begin_combs, end_combs, errors] = get_data()   # Read combination errors
    print(errors)
    print(rssis)

    rssi_max1 = max(rssis)                                          # Find 2 BSSIDs with highest RSSI values
    bssid_max1 = rssis.index(rssi_max1)
    rssis.remove(rssi_max1)
    rssi_max2 = max(rssis)
    bssid_max2 = rssis.index(rssi_max2)
    print(rssi_max1, rssi_max2)
    print(bssid_max1, bssid_max2)

    # for row in range(start_row, end_row+1):
    #     if sheet.cell(row=row, column=)

    #book_write.save('data\\data_comparison.xlsx')
    #print('BAP' + str(location) + ' saved.\n')



