#!/usr/bin/python3

# file-prefix.py - Write a program that finds all files with a given prefix,
# such as spam001.txt, spam002.txt, and so on, in a single folder and locates
# any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
# but no spam002.txt). Have the program rename all the later files to close this gap.

# As an added challenge, write another program that can insert gaps into
# numbered files so that a new file can be added.

import os, glob, shutil

# Takes in a user-defined directory and file prefix and returns a sorted array of the
# files in the directory that contain the prefix and three digts afterwards,
# independent of file extension
def get_glob(directory, prefix):
    path = os.path.join(directory, prefix)

    fileArray = glob.glob('{}[0-9][0-9][0-9].???'.format(path))
    fileArray.sort()
    return fileArray

#Takes in a sorted array of absolute path strings to numbered files and checks for gaps
# in the numbering, then fixes said gaps by renaming files
# TODO: Find a way to reduce number of lists used? Also, rename 'Arrays' to 'lists'
def update_numbering(array):
    intArray = []
    for filename in array:
        # get the three numbers from all filenames, and convert to an integer array
        dotIndex = filename.find('.')
        intArray.append(int(filename[(dotIndex - 3):dotIndex]))

    # find index of first item that isn't in the correct order (gapIndex)
    for i in range(len(intArray)):
        if intArray[i] != (i + 1):
            gapIndex = i
            break

    # create array of correctly numbered and formatted strings
    stringArray = intArray[gapIndex:]
    for i in range(len(stringArray)):
        stringArray[i] = str(i + 3).zfill(3)

    renameArray = array[gapIndex:]

    # (dotIndex -3):dotIndex of renameArray contains old file numbering
    # this builds the new filename for each file in the renameArray and renames it
    for i in range(len(renameArray)):
        newName = renameArray[i][:dotIndex - 3] + stringArray[i] + renameArray[i][dotIndex:]
        print("Renaming '{}' to '{}'".format(renameArray[i], newName))
        shutil.move(renameArray[i], newName)

# Prompt user for information
print("Please enter an option:\n")
print("UPDATE - Update the numbering of files in a directory")
print("NEW - Create a gap in numbered files for a new file\n")

choice = input()

while True:
    if choice.lower() == "update":
        # Get searchDirectory from user
        searchDirectory = input("Enter a directory to search:\n")
        while not os.path.exists(searchDirectory):
            searchDirectory = input('Search directory does not exist. Please try again:\n')

        # Get searchPrefix from user
        searchPrefix = input("Enter a file prefix to search for:\n")

        updateGlob = get_glob(searchDirectory, searchPrefix)
        update_numbering(updateGlob)
        break

    elif choice.lower() == "new":
        # Get searchDirectory from user
        searchDirectory = input("Enter a directory to search:\n")
        while not os.path.exists(searchDirectory):
            searchDirectory = input('Search directory does not exist. Please try again:\n')

        # Get searchPrefix from user
        searchPrefix = input("Enter a file prefix to search for:\n")
        print('New gap created!')
        break
    else:
        choice = input("Not a valid option. Please try again:\n")
