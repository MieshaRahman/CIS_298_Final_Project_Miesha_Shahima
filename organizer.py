import os
import shutil

folder_path = input("Enter the folder path you want to organize: ").strip()

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    print("Folder found successfully.")

    categories = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "PDFs": [".pdf"],
        "Documents": [".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".mov"],
        "Music": [".mp3", ".wav"],
        "Spreadsheets": [".csv", ".xlsx"],
        "Slides": [".pptx"],
        "Archives": [".zip", ".rar"]
    }

    file_counts = {}
    for category in categories:
        file_counts[category] = 0
    file_counts["Others"] = 0

    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
            print(f"Created folder: {category}")

    others_path = os.path.join(folder_path, "Others")
    if not os.path.exists(others_path):
        os.mkdir(others_path)
        print("Created folder: Others")

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Skip hidden/system files and only move regular files
        if os.path.isfile(file_path) and not file.startswith("."):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            try:
                for category, extensions in categories.items():
                    if file_ext in extensions:
                        shutil.move(file_path, os.path.join(folder_path, category, file))
                        print(f"Moved {file} -> {category}")
                        file_counts[category] += 1
                        moved = True
                        break

                if not moved:
                    shutil.move(file_path, os.path.join(folder_path, "Others", file))
                    print(f"Moved {file} -> Others")
                    file_counts["Others"] += 1

            except PermissionError:
                print(f"Skipped {file} because it is being used or permission was denied.")
            except Exception as e:
                print(f"Could not move {file}: {e}")

    print("\nSummary:")
    for category, count in file_counts.items():
        print(f"{category}: {count} files")

    print("File organization completed successfully!")

else:
    print("Invalid folder path. Please enter a valid existing folder.")