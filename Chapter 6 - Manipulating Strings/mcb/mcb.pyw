'''
import sys, shelve, pyperclip

mcbShelf = shelve.open("mcb")

#Save to clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    #delete key word
elif len(sys.argv) == 3 and sys.argv[1].lower == 'delete':
   # if sys.argv[2] in mcbShelf:
    del mcbShelf[sys.argv[2]]
#delete all
elif len(sys.argv) == 2:
    if sys.argv[1] == 'delete':
        del mcbShelf
#List key words and load content
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    else:
        pyperclip.copy(mcbShelf(sys.argv[1]))

mcbShelf.close()

'''

# ! python3
# mcb.pyw - Saves and Loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#       py.exe mcb.pyw list - loads all keywords to clipboard
#       py.exe mcb.pyx delete <keyword> - deletes specified keyword
#       py.exe mcb.pyx delete - deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()

    # Delete keywords specified in command line argument
elif len(sys.argv) == 3 and sys.argv[1].lower == "delete":
    del mcbShelf[sys.argv[2]]

    # Delete all keywords
elif len(sys.argv) == 2 and sys.argv[1].lower == "delete":
    del mcbShelf
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()