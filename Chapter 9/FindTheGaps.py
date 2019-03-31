#! python3
# Chapter 9 Project - Find the gaps in files with ascending numbers as a suffix

import re, os, shutil

# Compile the regex
searchClass = re.compile(r'''(
    ^(.*?)          # Prefix of filename
    ([0-9]{3})      # 3-digit increment
    (\.\w{2,4})$    # Suffix of filename Eg. .pdf .docx
)''', re.VERBOSE)

matches = []

# Search the current directory for matches
for filename in os.listdir(os.getcwd()):
    match = re.search(searchClass, filename)

    if match != None:
        print(match[0])