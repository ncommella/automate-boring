#!/usr/bin/python3

#mad-libs.py - Reads a text file, uses user input to create a mad lib to display
#and create a new text file.
#Usage: madlibs.py <input file> <output file> - runs and uses <input file> as the mad lib source file and outputs to the <output file>

import sys, os

#Open storyFile for reading via given <filename> in argument
if len(sys.argv) == 3 and os.path.exists(sys.argv[1]) and '.txt' in sys.argv[2]:
    storyFile = open(sys.argv[1])
#Notify user of improper use
else:
    print('ERROR: INVALID SYNTAX\nProper usage is "madlibs.py <input> <output>" where <input> is a valid path to a txt file and <output> is the name of an output .txt file')
    sys.exit()

#Parse through source for keywords & replace with user input
rawText = storyFile.read()
storyFile.close()
while 'ADJECTIVE' in rawText:
    rawText = rawText.replace('ADJECTIVE', input('Enter an adjective: '), 1)

while 'ADVERB' in rawText:
    rawText = rawText.replace('ADVERB', input('Enter an adverb: '), 1)

while 'NOUN' in rawText:
    rawText = rawText.replace('NOUN', input('Enter a noun: '), 1)

while 'VERB' in rawText:
    rawText = rawText.replace('VERB', input('Enter a verb: '), 1)

#display final mad lib and save new file
print(rawText)
finalFile = open(sys.argv[2], 'w')
finalFile.write(rawText)
finalFile.close()
