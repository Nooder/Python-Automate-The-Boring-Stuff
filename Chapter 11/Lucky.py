#! python3
# Chapter 11 Project - Opens several Google search results
# USAGE: Lucky.py <keyword list>      - Will google the joined phrase in arguments

import bs4, requests, sys, webbrowser

if len(sys.argv) < 2:
    print("USAGE: Lucky.py <keyword list>")
    sys.exit()

# Make the request
print("Googling...") # Display text while dowloading the pages
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Parse the links in the search result page
soup = bs4.BeautifulSoup(res.text, "lxml")
# Results will have the .r class and the link is in the anchor element
linkElements = soup.select(".r a")

# Get the first link and open it
firstLink = linkElements[0].get('href')
#print(firstLink)
webbrowser.open("http://google.com" + firstLink)