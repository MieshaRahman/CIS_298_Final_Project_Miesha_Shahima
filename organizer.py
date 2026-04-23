import os
import shutil

folder_path = input("Enter the folder path you want to organize: ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print("Folder found successfully.")

    categories = ["Images", "PDFs", "Documents", "Videos", "Music", "Others"]

    for category in categories:
        category_path = os.path.join(folder_path, category)

        if not os.path.exists(category_path):
            os.mkdir(category_path)
            print(f"Created folder: {category}")
else:
    print("Invalid folder path.")