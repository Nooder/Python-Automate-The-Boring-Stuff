#! python3
# Chapter 13 - Combines all the pdfs in the current working directory in to one pdf

import PyPDF2, os, logging

# Get all the .pdf files in the current directory
pdfs = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfs.append(filename)

pdfs.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pdf files
for pdf in pdfs:
    pdfFileObj = open(pdf, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages except the first and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the results to a pdf file
pdfOutput = open("meetingMinutes_MERGED.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()