#! python3
# Chapter 14 - Read all csv files in the current directory and remove the header row

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the directory searching for csvs
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # Skip non .csv files

    print("Removing header from %s" % csvFilename + "...")
    # Read the csv file in skipping the first row
    csvRows = []
    csvFileObj = open(csvFilename)
    csvReader = csv.reader(csvFileObj)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue    # Skip the first header row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the csv file
    csvFileObj = open(os.path.join("headerRemoved", csvFilename), 'w', newline="")
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

print("Done.")