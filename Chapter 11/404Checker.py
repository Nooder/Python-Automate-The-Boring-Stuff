#! python3
# Chapter 11 Project - Check for dead links on a website

import sys, requests, bs4, logging
logging.basicConfig(level=logging.INFO)

if len(sys.argv) < 2:
    print("USAGE: 404Checker.py <rootUrl>")

rootUrl = sys.argv[1]
error404List = []
allLinks = {""}

# Make the request
print("Checking for 404 errors on: %s..." % rootUrl)
res = requests.get(rootUrl)
res.raise_for_status()

# Get all the links on the page
html = bs4.BeautifulSoup(res.text, features="lxml")
links = html.select("a")
for link in links:
    print("Checking %s" % (link.get('href')))
    try:
        res = requests.get(link.get('href'))
        allLinks.add(link.get('href'))
        if res.status_code == 200:
            print("This link returned: " + str(res.status_code))
        elif res.status_code == 404:
            print("This link returned: " + str(res.status_code))
            error404List.append(link.get('href'))
        else:
            print("This link returned: " + str(res.status_code))
    except requests.exceptions.MissingSchema:
        res = requests.get(rootUrl + link.get('href'))
        allLinks.add(rootUrl + link.get('href'))
        if res.status_code == 200:
            print("This link returned: " + str(res.status_code))
        elif res.status_code == 404:
            print("This link returned: " + str(res.status_code))
            error404List.append(link.get('href'))
        else:
            print("This link returned: " + str(res.status_code))
    except:
        print("Failed to get webpage: %s" % link.get('href'))
        continue

# Link crawling

# crawledLinks = {""}
# for link in links:
#     if link not in crawledLinks:
#         try:
#             if link.get('href')[:4] != "http":
#                 link = "http:" + link.get('href')
#             res = requests.get(link.get('href'))
#             newHtml = bs4.BeautifulSoup(res.text, features="lxml")
#             newLinks = newHtml.select("a")
#             for newLink in newLinks:
#                 crawledLinks.add(newLink.get('href'))
#         except:
#             #print("Failed to get link: %s" % link.get('href'))
#             pass

# for i in crawledLinks:
#     print (i)
# print("Found %s links" % str(len(crawledLinks)))