#! python3
# Chapter 9 Project - Find all the large files through a walk from the current directory

import sys, os, shutil

print("Searching for files larger than 10MB: ")

# Walk the current directory
for folderName, subFolders, fileNames in os.walk('.'):
    for filename in fileNames:
        absPath = os.path.join(os.path.abspath(folderName), filename)
        if os.path.getsize(absPath) > 10000: # Find files larger than 10MB
            print(filename)