#! python3
# Chapter 18 Project - Show the current co-ordinates of the mouse

import pyautogui

print("Press Ctrl-C to quit.")

try:
    while True:
        # Get and print the mouse co-ordinates
        x, y = pyautogui.position()
        positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        # Get pixel RGB colours as well
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionString += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionString += ', ' + str(pixelColor[1]).rjust(3)
        positionString += ', ' + str(pixelColor[2]).rjust(3)
        print(positionString, end="")
        print('\b' * len(positionString), end='', flush=True)
except KeyboardInterrupt:
    print("\nDone.")