'''The OS module in Python provides functions for
    creating and removing a directory (folder),
    fetching its contents,
    changing and identifying the current directory, etc'''
import os


path='//Users/kkd/Downloads/NEW_FOLDER/INNER_FOLDER'   # For windows the path might look like 'D:/'.

if not os.path.exists(path):
    os.makedirs(path)
    print('All required directories have been created.')
else:
    print('Folder already exists.')