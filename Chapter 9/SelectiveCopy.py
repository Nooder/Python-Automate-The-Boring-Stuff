#!python3
# Chapter 9 Project - Copy all files of a certain type to a new folder
# USAGE: SelectiveCopy.py <filetype>                 - File type can be any type Eg. .pdf or .txt

import re, os, shutil

# Get filetype to search for from user
print("What type of file type do you want to copy to a new folder?")
filetype = str(input())

# Create directory to copy matching files to
print("Creating: [Copy of %s] directory" % (filetype))
os.makedirs("Copy of " + filetype)

# Create regex to find file type
searchString = r'(.*?)(' + filetype + ')$'
searchClass = re.compile(searchString)

matches = []

for folderName, subFolders, fileNames in os.walk('.'):
    # Check for matches to regex
    for filename in fileNames:
        match = re.search(searchClass, filename)
        if match != None:
            matches.append(match[0])

for match in matches:
    print("-> Copying %s" % (match))
    shutil.copy(match, "Copy of " + filetype)

print("Done.")