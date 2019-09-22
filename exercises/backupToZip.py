#!/usr/bin/python3
#backupToZip.py - backs up a folder to a zip file whose name increments

import zipfile, os

def backupToZip(folder):
    #backup the entire contents of 'folder' into a zip zipfile
    folder = os.path.abspath(folder) #Make sure path is absolute

    #Figure out what filename this code should use based on what filenames exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Now creating {}...'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print ('Adding files in {}...'.format(foldername))
        # Add the current folder to the ZIP files
        backupZip.write(foldername)
        # Add all the files in the folder to the ZIP file
        for file in filenames:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue #Don't add other backup files to new backup zipfile
            backupZip.write(os.path.join(foldername, file))
    backupZip.close()
    print('Done.')

target = input('Enter a folder to backup:\n')
backupToZip(target)
