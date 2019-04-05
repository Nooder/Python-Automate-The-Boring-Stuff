#! python3
# Chapter 15 Project - Stopwatch and lap timer

import time, logging

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. \
Press Ctrl-C to quit.')
input()                     # Press <Enter> to begin
print("Started.")
startTime = time.time()     # Get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl+C keybpard interrupt to prevent the error message displaying
    print("\nDone.")