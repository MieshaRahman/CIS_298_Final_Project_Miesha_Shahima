# Python File Organizer Tool

## Team Members
- Miesha  
- Shahima  

---

## Project Description
This project is a Python File Organizer Tool that automatically organizes files in a selected folder into categories such as Images, Documents, Videos, Music, and more. The program improves file management by sorting files based on their extensions.

---

## Features
- Automatically organizes files into folders
- Supports multiple file types
- Creates folders if they do not exist
- Skips hidden/system files
- Handles permission errors safely
- Displays summary of moved files
- User-friendly messages

---

## How to Run
1. Open the project in PyCharm  
2. Open `organizer.py`  
3. Run the program  
4. Enter the full folder path when prompted  
5. Files will be organized automatically  

---

## User Manual
- Run the program using `organizer.py`
- Enter a valid folder path
- The program creates folders for each file category
- Files are moved into corresponding folders
- A summary is displayed after execution

---

## Supported File Types
- **Images:** .jpg, .png, .jpeg, .gif  
- **PDFs:** .pdf  
- **Documents:** .docx, .txt, .doc  
- **Videos:** .mp4, .mov  
- **Music:** .mp3, .wav  
- **Spreadsheets:** .csv, .xlsx  
- **Slides:** .pptx  
- **Archives:** .zip, .rar  
- **Others:** Any unsupported file type  

---

## Testing Notes
- Tested with different file types  
- Verified correct folder creation  
- Confirmed proper file movement  
- Tested invalid folder paths  
- Checked summary output accuracy  

---

## Troubleshooting
- Ensure the folder path is correct  
- Avoid using system folders like `C:\`  
- Close files that may be in use  
- Make sure Python interpreter is configured  

---

## Work Log

Work Session 1 - Miesha  
Time Spent: 45 minutes  
- Created GitHub repository  
- Added Shahima as collaborator  
- Cloned project into PyCharm  
- Created initial `organizer.py` file  
- Implemented basic folder path validation  

---

Work Session 2 - Shahima  
Time Spent: 30 minutes  
- Implemented category folder creation (Images, PDFs, Documents, Videos, Music, Others)  
- Ensured folders are created only if they do not exist  
- Tested folder creation functionality  

---

Work Session 3 - Miesha  
Time Spent: 40 minutes  
- Added file extension detection using `os.path.splitext()`  
- Implemented file moving logic using `shutil.move()`  
- Organized files into appropriate category folders  
- Tested file sorting functionality  

---

Work Session 4 - Shahima  
Time Spent: 30 minutes  
- Added support for additional file types (GIF, DOC, MOV, WAV, CSV, XLSX, PPTX)  
- Expanded categories to include Spreadsheets and Slides  
- Tested updated file categorization  

---

Work Session 5 - Miesha  
Time Spent: 20 minutes  
- Improved user input handling using `.strip()`  
- Reduced input errors caused by extra spaces  
- Retested program with different folder paths  

---

Work Session 6 - Shahima  
Time Spent: 30 minutes  
- Implemented file count tracking for each category  
- Added summary output displaying number of files moved  
- Improved output readability for users  

---

Work Session 7 - Miesha  
Time Spent: 15 minutes  
- Added logic to skip hidden/system files  
- Prevented errors from processing restricted files  
- Tested behavior with system files  

---

Work Session 8 - Shahima  
Time Spent: 10 minutes  
- Improved error message for invalid folder paths  
- Made program output more user-friendly  
- Tested invalid input scenarios  

---

Work Session 9 - Miesha  
Time Spent: 10 minutes  
- Added support for archive file types (.zip, .rar)  
- Updated categorization logic to include Archives  
- Verified correct movement of archive files  

---

Work Session 10 - Shahima  
Time Spent: 10 minutes  
- Performed final code cleanup and formatting  
- Improved README documentation  
- Verified overall program functionality  
- ---

## Final Notes
- This project demonstrates file handling using Python
- It improves file organization automatically
- Future improvements may include GUI support and more file categories
