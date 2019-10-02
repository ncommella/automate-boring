#!/usr/bin/python3

# file-prefix.py - Write a program that finds all files with a given prefix,
# such as spam001.txt, spam002.txt, and so on, in a single folder and locates
# any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
# but no spam002.txt). Have the program rename all the later files to close this gap.

# As an added challenge, write another program that can insert gaps into
# numbered files so that a new file can be added.

import os, glob

def update_files(directory, prefix):
    path = os.path.join(directory, prefix)

    fileArray = glob.glob('{}???.txt'.format(path))
    fileArray.sort()
    print(fileArray)
            
    # TODO: Walk through directory
    # TODO: search for files containing prefix
        # TODO: analyze numbering, looking for gaps in numbering
            # TODO: renumber all files after gap

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

        update_files(searchDirectory, searchPrefix)
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
