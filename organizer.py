import os
import shutil

folder_path = input("Enter the folder path you want to organize: ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print("Folder found successfully.")
else:
    print("Invalid folder path.")