#!/usr/bin/python3
# regex.py - Opens all .txt files in a specified directory and searches them for
# a user-defined regular expression. Uses interactive prompts rather than arguments
# Usage: ./regex.py

import re, os, sys

#Get directory from user & validate it
while True:
    targetDirectory = input('Enter the directory to search: \nType "quit" to exit\n')
    if targetDirectory.lower() == 'quit':
        sys.exit()
    #Continue with search if valid directory
    if os.path.isdir(targetDirectory):
        os.chdir(targetDirectory)
        #Get regex from user
        regexTarget = re.compile(input('Enter a regular expression to search for:\n'))
        # TODO: Validate regex
        #Open each .txt file in directory and search for regex
        for fileName in os.listdir(targetDirectory):
            if fileName.endswith('.txt'):
                textFile = open(fileName)
                #Display results
                # TODO: show what file each result is from
                print(regexTarget.findall(textFile.read()))
    else:
        print('That is not a valid directory. Please try again')
