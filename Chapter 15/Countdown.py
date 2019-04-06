#! python3
# Chapter 15 Project - Countdown timer with an alarm

import time, subprocess

timeLeft = 3
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file
subprocess.Popen(['see', 'alarm.wav'])