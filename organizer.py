import os
import shutil

folder_path = input("Enter the folder path you want to organize: ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print("Folder found successfully.")

    categories = {
        "Images": [".jpg", ".png", ".jpeg"],
        "PDFs": [".pdf"],
        "Documents": [".docx", ".txt"],
        "Videos": [".mp4"],
        "Music": [".mp3"]
    }

    # Create category folders
    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
            print(f"Created folder: {category}")

    # Create Others folder
    others_path = os.path.join(folder_path, "Others")
    if not os.path.exists(others_path):
        os.mkdir(others_path)
        print("Created folder: Others")

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            try:
                for category, extensions in categories.items():
                    if file_ext in extensions:
                        shutil.move(file_path, os.path.join(folder_path, category, file))
                        print(f"Moved {file} -> {category}")
                        moved = True
                        break

                if not moved:
                    shutil.move(file_path, os.path.join(folder_path, "Others", file))
                    print(f"Moved {file} -> Others")

            except PermissionError:
                print(f"Skipped {file} because it is being used or permission was denied.")
            except Exception as e:
                print(f"Could not move {file}: {e}")

    print("File organization completed.")

else:
    print("Invalid folder path.")