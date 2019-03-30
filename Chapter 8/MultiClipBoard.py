#! python3
# Chapter 8 Project - Create a clipboard to read, save and load clipboard data to and from a file
# Usage: python3 MultiClipBoard.py save <keyword> - Saves clipboard to keyword
#        python3 MultiClipBoard.py <keyword> - Loads keyword to clipboard
#        python3 MultiClipBoard.py list - Loads all keywords to clipboard
#        python3 MultiClipBoard.py delete <keyword> - Delete keyword from file
#        python3 MultiClipBoard.py delete - Delete all keywords from the file

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords, load and delete content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for key in mcbShelf.keys():
            del mcbShelf[key]

mcbShelf.close()