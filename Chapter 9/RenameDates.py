#! python3
# Chapter 9 Project - Find all American style dates and rename them to European style dates
# US Format: MM-DD-YYYY     EU Format: DD-MM-YYYY

import shutil, re, os

# Regex to match American date format
datePattern = re.compile(r"""(
    ^(.*?)                  # All text before the date
    ((0|1)?\d)-             # One or two digits for the month
    ((0|1|2|3)?\d)-         # One or two digits for the day
    ((19|20)\d\d)           # Four digits for the year
    (.*?)$                  # All text after the date
)""", re.VERBOSE)

# Loop over the files in the working directory
for americanFilename in os.listdir("."):
    match = datePattern.search(americanFilename)

    # Skip files without dates
    if match == None:
        continue
    
    # Get the different part of the filenames for the matches
    beforePart = match.group(1)
    monthPart = match.group(2)
    dayPart = match.group(4)
    yearPart = match.group(6)
    afterPart = match.group(8)

    # Form the European style filename
    europeanFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full absolute filepaths
    absoluteWorkingDirectory = os.path.abspath('.')
    americanFilename = os.path.join(absoluteWorkingDirectory, americanFilename)
    europeanFilename = os.path.join(absoluteWorkingDirectory, europeanFilename)

    # Rename the files
    print("Renaming '%s' to '%s'..." % (americanFilename, europeanFilename))
    #shutil.move(americanFilename, europeanFilename) # uncomment after testing and verifying