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
        matches.append(match[3])

matches.sort()
incrementCounter = 1
incrementsProperly = True

for suffix in matches:
    if int(suffix) == incrementCounter:
        incrementCounter += 1
        continue
    else:
        incrementsProperly = False
        break

print(matches)
print("Has proper increments: " + str(incrementsProperly))