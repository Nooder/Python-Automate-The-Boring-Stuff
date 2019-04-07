#! python3
# Chapter 17 Project - Find all folders on disk that are mainly photos

import os, logging
from PIL import Image

photoFolders = []

# Loop through each folder to check for photos
for folderName, subFolders, filenames in os.walk('/'):
    photoCount = 0
    totalFiles = 0
    #print("Checking: %s..." % os.path.join(os.path.abspath(folderName)))
    for filename in filenames:
        #print(os.path.join(os.path.abspath(folderName), filename))
        # Check for image filetypes
        if filename.endswith('jpg') or filename.endswith('png')\
            or filename.endswith('.gif'):
            try:
                image = Image.open(os.path.join(os.path.abspath(folderName), filename))
            except:
                logging.info("Couldn't open %s" %\
                    os.path.join(os.path.abspath(folderName), filename))
            width, height = image.size
            if width > 500 or height > 500:
                photoCount += 1
            totalFiles += 1
        else:
            totalFiles += 1
    
    # Check to see if more than half of the files were photos
    if photoCount == 0 or totalFiles == 0:
        continue
    if photoCount / totalFiles > 0.5:
        print("Found photo folder: %s" % os.path.join(os.path.abspath(folderName)))
        photoFolders.append(os.path.join(os.path.abspath(folderName)))

print("Done.")