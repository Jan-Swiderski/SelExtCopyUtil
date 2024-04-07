# SelExtCopyUtil
## Overview

`SelExtCopyUtil` is a tool that enables users to copy files with a specific extension from a source directory to a destination directory, utilizing a graphical interface for ease of use. It allows for the selection of desired file extensions and the addition of a prefix and date to the name of the destination folder. This utility is designed for those who need a straightforward solution for organizing or backing up files based on their extensions.
s with the extension in any case.
	**Folder Prefix**: Enter a prefix for the name of the new folder that will be created in the destination directory. The folder's name will also include the current date in the selected format.
	**Select Date Format**: Choose a date format from the dropdown menu for the folder name in the destination directory. The available options are `YYYY-MM-DD`, `DD-MM-YYYY`, and `MM-DD-YYYY`.**Run**: Click the "Run" button to start the copying process. The application will create a new folder in the destination directory, named with the chosen prefix and date, and will copy all files with the specified extension into this folder.
	**Completion**: Once the copying process is completed, a message box will inform you of the success. The application will then automatically close.
## Running and editing the Python code
### Setting up the Environment and Installation
This project is designed to run with a standard Python environment, making it accessible and easy to set up. Here's how to get your environment ready and run the project.
### Prerequisites
- **Python:** Ensure you have Python installed on your system. The project requires Python 3.6 or newer, but Python 3.12.2 is recommended for the best compatibility and performance. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/) or install it using your system's package manager. This project uses standard Python libraries, including `tkinter` for the GUI components, which is included in the standard Python distribution.

- **Environment:** You can use any standard Python environment, including virtual environments created with `venv` or `conda` environments. If you're using `conda`, you can create a new environment using the following command:
  ```
  conda create --name myenv python=3.12.2
  ```
  Replace `myenv` with your preferred environment name. Adjust the Python version according to your preferences, though 3.12.2 is recommended.

### Installation

No additional installations are required for this project as it solely depends on the standard Python library. 
### Running the Application
1. **Activate your environment** (if using virtualenv or conda):
   - For `venv`:
     ```
     source myenv/bin/activate
     ```
     On Windows:
     ```
     myenv\Scripts\activate
     ```
   - For `conda`:
     ```
     conda activate myenv
     ```

2. **Navigate to the project directory** where the script is located.

3. **Run the script** using Python:
   ```
   python sel_ext_copy_util.py
   ```
## Limitations
When using `SelExtCopyUtil`, it is important to ensure that the source and destination directories are not the same. Specifically, if a destination folder (defined by a prefix and date format) is created within the source directory, the application will attempt to copy files into this newly created subdirectory. However, as the application continues to scan the source directory, it may encounter this destination subdirectory and attempt to copy its contents again, leading to errors. This recursive copying attempt can generate errors like '... are the same file' or 'Permission denied' as the application tries to overwrite files within the same directory structure.

For example, if the source directory is `C:\Users\ExampleUser\Documents` (on Windows) or `/Users/ExampleUser/Documents` (on macOS) and the destination directory is configured to be a subdirectory of the source, errors will occur when the application attempts to copy files from the source into the source itself, now considered part of the destination.

To avoid this issue, always ensure that the destination directory is outside of the source directory or select a source directory that does not contain the destination directory as a subdirectory.
## License
This project is licensed under the MIT License.
Feel free to modify and customize the script to fit your specific requirements.
## Responsibility disclaimer
Author of the script do not take any responsibility for any losses made by script and its usage. User uses the script on own responsibility.