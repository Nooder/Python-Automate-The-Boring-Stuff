# Chapter 8 Project - Generate mad libs based on an input text file with keywords

import re, shelve, sys, os

# Open the madlib file to modify (Contains NOUN, ADJECTIVE, VERB, ADVERB)
try:
    madlibFile = open(os.path.relpath('MadLibs Files' + os.path.sep + 'madlib.txt'))
except FileNotFoundError:
    print("ERROR: Please make sure the file to edit is in ./MadLibs Files/madlib.txt")
    sys.exit()

text = madlibFile.read()

# Get inputs from user (unique to this file)
print("Enter an adjective:")
firstAdjective = input()
print("Enter a noun:")
firstNoun = input()
print("Enter a verb:")
firstVerb = input()
print("Enter a noun:")
secondNoun = input()

# Compile regex for each class
nounRegex = re.compile('NOUN')
adjectiveRegex = re.compile('ADJECTIVE')
verbRegex = re.compile('VERB')
adverbRegex = re.compile('ADVERB')

# Perform substitution
text = re.sub('ADJECTIVE', firstAdjective, text, count=1)
text = re.sub('NOUN', firstNoun, text, count=1)
text = re.sub('VERB', firstVerb, text, count=1)
text = re.sub('NOUN', firstNoun, text, count=1)

# Write the results to a new file
print(text)
writeFile = open(os.path.relpath('MadLibs Files' + os.path.sep + "madlib_EDITED.txt"), 'w')
writeFile.write(text)