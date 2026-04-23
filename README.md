# Python File Organizer Tool

## Team Members
- Miesha
- Shahima

## Project Description
This project is a Python File Organizer Tool. It organizes files in a selected folder into categories such as Images, PDFs, Documents, Videos, Music, Spreadsheets, Slides, Archives, and Others using Python libraries.

## Libraries Used
- os
- shutil

---

## Features
- Organizes files automatically based on file type
- Supports multiple file formats (images, documents, videos, music, etc.)
- Creates folders if they do not exist
- Skips hidden/system files
- Handles permission errors safely
- Displays summary of files moved
- Provides user-friendly messages

---

## How to Run
1. Open `organizer.py`
2. Run the program
3. Enter the folder path you want to organize
4. The program will sort files into folders automatically

---

## Work Log

### Work Session 1 - Miesha
Time Spent: 45 minutes
- Created the GitHub repository
- Added Shahima as collaborator
- Cloned project in PyCharm
- Added organizer.py
- Implemented folder path validation

---

### Work Session 2 - Shahima
Time Spent: 30 minutes
- Added category folders (Images, PDFs, Documents, Videos, Music, Others)
- Tested folder creation functionality

---

### Work Session 3 - Miesha
Time Spent: 40 minutes
- Added file extension detection
- Implemented file moving logic
- Added error handling for restricted files
- Tested sorting functionality

---

### Work Session 4 - Shahima
Time Spent: 30 minutes
- Added support for additional file types (GIF, DOC, MOV, WAV, CSV, XLSX, PPTX)
- Improved category structure
- Tested updated sorting

---

### Work Session 5 - Miesha
Time Spent: 20 minutes
- Improved input handling using `.strip()`
- Tested user input validation

---

### Work Session 6 - Shahima
Time Spent: 30 minutes
- Added summary count of moved files
- Displayed categorized file counts
- Improved output readability

---

### Work Session 7 - Miesha
Time Spent: 15 minutes
- Added check to skip hidden/system files
- Prevented unnecessary processing errors

---

### Work Session 8 - Shahima
Time Spent: 10 minutes
- Improved invalid folder error message
- Enhanced user experience

---

### Work Session 9 - Miesha
Time Spent: 10 minutes
- Added support for archive files (.zip, .rar)
- Expanded file categorization

---

### Work Session 10 - Shahima
Time Spent: 10 minutes
- Added final success message
- Improved overall program usability
- ---

## How to Run

1. Open the project in PyCharm.
2. Open the file named `organizer.py`.
3. Run the program.
4. Enter the full path of the folder you want to organize.
5. The program will create category folders and move files into the correct folders.
6. ---

## User Manual

- Run the program using `organizer.py`.
- Enter a valid folder path when prompted.
- The program will automatically create folders for different file types.
- Files will be moved into their respective folders.
- A summary will be displayed showing how many files were moved.
- ---

## Supported File Types

- Images: .jpg, .png, .jpeg, .gif  
- PDFs: .pdf  
- Documents: .docx, .txt, .doc  
- Videos: .mp4, .mov  
- Music: .mp3, .wav  
- Spreadsheets: .csv, .xlsx  
- Slides: .pptx  
- Archives: .zip, .rar  