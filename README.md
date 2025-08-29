
# Python File Organizer Script
---
## About
This is a simple yet powerful command-line script that automatically organizes files in a directory. It sorts all files into new subdirectories based on their **file extensions**, making it an excellent tool for cleaning up messy folders like your Downloads or Desktop. 🧹

---
## How to Use
### Prerequisites
* **Python 3.x** installed on your computer.

### Instructions
1.  **Save the Script:** Save the provided Python code into a file named `organize_files.py` on your computer.
2.  **Open Your Terminal:**
    * **Windows:** Open Command Prompt or PowerShell.
    * **macOS/Linux:** Open the Terminal application.
3.  **Navigate to the Script's Location:** Use the `cd` (change directory) command to move to the folder where you saved the `organize_files.py` file.
4.  **Run the Script:** Execute the script from the command line, providing the path to the directory you want to organize as an argument.

---
## Usage
The script's basic usage is as follows:

```

python organize_files.py \<directory\_path\>

```
Replace `<directory_path>` with the absolute or relative path to the folder you want to clean up.

### Examples
**Windows:**
```

python organize_files.py "C:\\Users\\YourUsername\\Downloads"

```
**macOS / Linux:**
```

python organize_files.py /home/YourUsername/Documents/MyFiles

```

---
## Features
* **Organizes by Extension:** Creates new folders for each unique file extension (e.g., `pdf`, `jpg`, `txt`).
* **Handles Files Without Extensions:** Places files like `README` into a dedicated `no_extension` folder.
* **Skips Directories:** The script intelligently ignores existing folders and symbolic links, ensuring they are not moved.
* **Robust Error Handling:** It will notify you if a directory is not found or if there is an issue moving a specific file without crashing the entire process.
