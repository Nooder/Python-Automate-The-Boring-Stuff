#! python3
# Chapter 13 Project - Try to brute force a pdf password
# USAGE: PdfCracker.py <filename>    # pdf to crack

import PyPDF2, os, sys, logging

# Setup
if len(sys.argv) < 2:
    print("USAGE: PdfCracker.py <filename>")
    sys.exit()

filename = sys.argv[1]
dictionary = open("dictionary.txt", 'r')
words = dictionary.readlines()
pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))

# Try to decrypt using each word in the dictionary
print("Decrypting...")
for word in words:
    if pdfReader.decrypt(word):
        print("  -> Successfully decrypted with password: %s" % word)

if pdfReader.isEncrypted:
    print("Could not decrypt the file with basic dictionary words...")

print("Done.")