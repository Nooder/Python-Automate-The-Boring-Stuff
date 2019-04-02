#!python3
# Chapter 11 Project - Pull up google maps to search a given address
# USAGE: MapIt.py <address>

import sys, webbrowser

# Check to make sure command line args exist for the address
if len(sys.argv) < 1:
    print("USAGE: MapIt.py <address>")
    sys.exit()

# Build the search URL for google maps
baseURL = "https://www.google.com/maps/place/"
address = "+".join(sys.argv[1:])
searchURL = baseURL + address

webbrowser.open(searchURL)