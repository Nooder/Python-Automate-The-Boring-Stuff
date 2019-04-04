#! python3
# Chapter 12 Project - Tabulates population and number of census tracts for each county.

import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}

print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure there is a key for the state
    countyData.setdefault(state, {})
    # Make sure there is a key for the county for this state
    countyData[state].setdefault(county, {'tracts' : 0, 'pop': 0})

    # Each row represents one census tract, so increment it by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it
print("Writing results...")
resultFile = open("census2010.py", 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print("Done.")