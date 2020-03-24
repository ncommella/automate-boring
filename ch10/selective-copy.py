#!/usr/bin/python3

# selective-copy.py - Write a program that walks through a folder tree and
# searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import os, shutil

def selectiveCopy(source, extension, target):
    #Walk the giuven source directory
    for folderName, subFolders, filenames in os.walk(source):
        # Iterate through files looking for the desired extension
        for filename in filenames:
            if filename.endswith(extension):
                # Copy Identified file to the target directory
                # print('Moving {} to {}'.format(os.path.join(folderName, filename), target))
                shutil.copy(os.path.join(folderName, filename), target)

#Prompt User for information
callSource = input('Enter the source directory to search:\n')
while not os.path.exists(callSource):
    callSource = input('Source directory does not exist. Please try again:\n')

callExtension = input('Enter the file extension to look for (e.g. ".txt"):\n')
# TODO: add input validation for file extension

callTarget = input("Enter the target directory you'd like the files copied to:\n")
while not os.path.exists(callTarget):
    callTarget = input('Target directory does not exist. Please enter a valid directory:\n')

print('')
selectiveCopy(callSource, callExtension, callTarget)
