#! python3
# Chapter 17 Project - Resize images in directory and add a logo to each

import os, logging
from PIL import Image

# Setup
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

logoImage = Image.open(LOGO_FILENAME)
logoImage = logoImage.resize((50,50))
logoWidth, logoHeight = logoImage.size

# Directory to store the results
os.makedirs('WithLogo', exist_ok=True)
# Loop through all images in the directory
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg'))\
        or filename == LOGO_FILENAME:
        continue       # Skip non image files and the logo file itself

    image = Image.open(filename)
    width, height = image.size

    # Check if the image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print("Resizing %s..." % filename)
        image = image.resize((width, height))

        # Add the logo
        print("Adding the logo to %s..." % filename)
        image.paste(logoImage, (width - logoWidth, height - logoHeight), logoImage)

        # Save changes
        image.save(os.path.join('WithLogo', filename))