#!/usr/bin/python3

#mcb.pyw -- Saves and loads pieces of text to the clipboard
#Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
#       mcb.pyw <keyword> - Loads keyword to clipboard
#       mcb.pyw list - Loads all keywords to clipboard
#       mcb.pyw delete <keyword> - deletes keyword from data file

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('Saved \"{}\" as {}'.format(mcbShelf[sys.argv[2]], sys.argv[2]))
#Check for 'Delete' <keyword>
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    print(str(sys.argv[2]) + ' deleted!')
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('List copied to clipboard')
    # TODO: check for deleteAll keyword
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('{} added to clipboard'.format(sys.argv[1]))

mcbShelf.close()
