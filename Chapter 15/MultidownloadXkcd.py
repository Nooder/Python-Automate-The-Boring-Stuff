#! python3
# Chapter 15 Project - Multithreaded XKCD comic downloader

import requests, os, bs4, threading, logging

os.makedirs('xkcd', exist_ok=True)      # Store the comics in the ./xkcd folder

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic +1):
        # Download the page
        print("Downloading page http://xkcd.com/%s" % urlNumber)
        try:
            res = requests.get('http://xkcd.com/%s' % urlNumber)
        except requests.exceptions.MissingSchema:
            print("Couldn't download: http://xkcd.com/%s" % urlNumber)
            continue
        #res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "lxml")
        
        # Find url of the comic image
        comicElement = soup.select('#comic img')
        if comicElement == []:
            print("Could not find comic image.")
        else:
            comicUrl = comicElement[0].get('src')
            # Download the image
            print("Downloading image %s..." % comicUrl[2:])
            try:
                res = requests.get("http://" + comicUrl[2:])
            except requests.exceptions.MissingSchema:
                print("Couldn't download: %s" % comicUrl[2:])
                continue
            #res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the thread objects
downloadThreads = []            # A list of all the thread objects
for i in range(0, 1400, 100):   # Loops 14 times - creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")