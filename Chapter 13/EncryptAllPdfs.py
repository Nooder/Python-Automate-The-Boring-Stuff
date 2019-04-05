#!python3
# Chapter 13 Project - Encrypt all pdfs in current directory including subfolders
# USAGE: EncryptAllPdfs.py <password>   # Password to encrypt all pdf files with

import PyPDF2, os, sys, logging

# Setup
if len(sys.argv) < 2:
    print("USAGE: EncryptAllPdfs.py <password>")
    sys.exit()

password = sys.argv[1]    
pdfs = []
encryptedPdfs = []
for folderName, subFolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfs.append(filename)

# Loop through the pdfs and encrypt each one
for filename in pdfs:
    print("Encrypting ")
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    outputFile = open(filename[:-4] + "_ENCRYPTED.pdf", 'wb')
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    pdfWriter.write(outputFile)

print("Done.")