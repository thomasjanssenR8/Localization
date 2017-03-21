"""
6-Bachelor thesis: Wi-Fi localization - Thomas Janssen
Localization v3: Collect BSSIDs in your vicinity
"""

import subprocess
import openpyxl

cmd_output = subprocess.check_output('netsh wlan show networks mode=bssid')
cmd = cmd_output.decode('UTF-8')                            # Get CMD output
# print(cmd)
bssids = []
strengths = []

index = i = 0
while cmd.find("BSSID", index + i) != -1:                   # Find all BSSIDs
    index = cmd.find("BSSID", index + i)                    # index of first letter that matches the string
    bssids.append(cmd[(index + 26):index + 43])             # 26-43 = BSSID (network MAC-adres)
    strengths.append(int(cmd[(index + 75):(index + 77)]))   # Signal strength in %
    i += 1

print(bssids)
print(strengths)

# Get coordinates of your position
measuredLatitude = float(input("Give the latitude of the coordinate you measured: "))
measuredLongitude = float(input("Give the longitude of the coordinate you measured: "))


# Save data to Excel sheet
file = 'bssids.xlsx'
book = openpyxl.load_workbook(filename=file)
sheet = book.active

count = 0
rowindex = sheet.max_row + 2
while count < len(bssids):
    Aindex = 'A' + str(rowindex)
    Bindex = 'B' + str(rowindex)
    Cindex = 'C' + str(rowindex)
    Dindex = 'D' + str(rowindex)
    sheet[Aindex] = bssids[count]
    sheet[Bindex] = strengths[count]
    sheet[Cindex] = measuredLatitude
    sheet[Dindex] = measuredLongitude
    count += 1
    rowindex += 1

book.save(file)


















