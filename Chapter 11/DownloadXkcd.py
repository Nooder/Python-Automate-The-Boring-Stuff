#! python3
# Chapter 11 Project - Download all the xkcd comics

import os, bs4, requests

url = 'http://xkcd.com'             # Starting URL
os.makedirs("xkcd", exist_ok=True)  # Store comics in ./xkcd
while not url.endswith("#"):
    # Download the page
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image
    comicElement = soup.select("#comic img")
    if comicElement == []:
        print("Could not find the comic image.")
    else:
        try:
            comicUrl = "http:" + comicElement[0].get("src")
            # Download the image
            print("Downloading image %s..." % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip this comic
            previousLink = soup.select('a[rel="prev]"')[0]
            url = 'http://xkcd.com' + previousLink.get('href')
            continue

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the previous link's URL
    previousLink = soup.select('a[rel="prev]"')[0]
    url = 'http://xkcd.com' + previousLink.get('href')

print("Done.")