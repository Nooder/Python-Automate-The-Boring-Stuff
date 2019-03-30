# Chapter 8 Project - Search a directory for all matches to a regex on .txt files

import re, os, sys

textFiles = []
matches = []

# Get regex string from user
print("Enter the regex to search for in this dir:")
regex = str(input())
reClass = re.compile(regex)

# Walk through each file in the current dir
for file in os.listdir():
    txtRegex = re.compile(r'\.txt$')
    try:
        if re.search(txtRegex ,file)[0]:
            textFiles.append(file)
    except TypeError:
        pass

# Loop through .txt files and search for the regex matches
for file in textFiles:
    searchFile = open(file)
    text = searchFile.readlines()
    text = ''.join(text)
    regex = ".*" + regex + ".*"
    matchesInFile = re.search(regex, text)
    if matchesInFile:
        print("Match in file: " + file)
        print(matchesInFile[0])