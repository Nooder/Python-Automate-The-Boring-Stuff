#! python3
# Chapter 9 Project - Backup a folder in to a zip file with auto-incrementing values

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of the folder in to a zip file

    folder = os.path.abspath(folder) # make sure folder path is absolute

    # Figure out the auto-increment part of the filename for this file
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file
    print("Creating %s..." % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and add each folder and file to the zip file
    for folderName, subFolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (folderName))
        # Add the current folder to the zip file
        backupZip.write(folderName)
        # Add all the files in this folder to the zipfile
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Don't backup the backup zip files
            backupZip.write(os.path.join(folderName, filename))
    
    backupZip.close()
    print("Done.")

backupToZip("Test Backup")