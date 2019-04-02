#! python3
# Chapter 11 Project - Examples parsing HTML files with BeautifulSoup

import bs4

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
elements = exampleSoup.select("#author")
print("Type of 'elements: %s" % str(type(elements)))
print("Length of 'elements: %s" % str(len(elements)))
print("Type of 'elements[0]: %s" % str(type(elements[0])))
print("elements[0].getText(): %s" % str(elements[0].getText()))
print("str(elements[0]): %s" % str(elements[0]))
print("elements[0].attrs: %s" % str(elements[0].attrs))