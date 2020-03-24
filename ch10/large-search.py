#!/usr/bin/python3

# large-search.py - Write a program that walks through a folder tree and searches
# for exceptionally large files or folders—say, ones that have a file size of
# more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize()
# from the os module.) Print these files with their absolute path to the screen.

import os

def search(directory):
    #Walk the given source directory
    for folderName, subFolders, filenames in os.walk(directory):
        # Iterate through files, measuring size, and printing abspath if over 100MB
        for filename in filenames:
            path = os.path.join(folderName, filename)
            size = os.path.getsize(path)
            if (size / 1000000) > 100:
                print('{} is {}MB'.format(path, size // 1000000)) #round figure

#Prompt User for information
callDirectory = input('Enter the source directory to search:\n')
while not os.path.exists(callDirectory):
    callDirectory = input('Source directory does not exist. Please try again:\n')

search(callDirectory)
