#! python3
# Chapter 6 Project - Add bullet points to each line of text in the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and prefix each with a star
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = "* " + lines[i]

# Join the list back in to a string for pyperclip to copy
text = "\n".join(lines)

pyperclip.copy(text)