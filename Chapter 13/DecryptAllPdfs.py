#! python3
# Chapter 13 Project - Decrypt all pdfs in current directory including subfolders
# USAGE: DecryptAllPdfs.py <password>   # Password to decrypt all pdf files with

import PyPDF2, os, sys, logging

# Setup
if len(sys.argv) < 2:
    print("USAGE: DecryptAllPdfs.py <password>")
    sys.exit()

password = sys.argv[1]
pdfs = []

# Find all encrypted pdfs
for folderName, subFolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
            if pdfReader.isEncrypted:
                print("Decrypting: %s ... " % filename, end="")
                pdfReader.decrypt(password)
                print("Done.")
                print("  -> Writing to: %s" % filename[:-4] + "_DECRYPTED.pdf... ", end="")
                outputFile = open(filename[:-4] + "_DECRYPTED.pdf", 'wb')
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.write(outputFile)
                print("Done.")
                outputFile.close()

print("All pdfs decrypted.")