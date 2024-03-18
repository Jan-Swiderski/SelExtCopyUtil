import os
import shutil
from datetime import datetime
from tkinter import Tk, simpledialog, filedialog, messagebox

def copy_files_with_extension(source_path: str, destination_path: str, extension: str):
    """
    The function copies files with the given extension from the source directory to the destination directory.
    It iterates through each file in the source directory, including subdirectories. If a file ends with
    the specified extension, it is copied to the destination directory.

    Params:
    - source_path (str): The path to the directory where the source files are located.
    - destination_path (str): The path to the directory where the files should be copied.
    - extension (str): The file extension to filter files by. Only files with this extension will be copied.

    """
    # Walk through the directory tree starting from source_path
    for root, dirs, files in os.walk(source_path):
        # Iterate over each file in the directories
        for file in files:
            # Check if the file ends with the given extension
            if file.endswith(extension.upper()) | file.endswith(extension.lower()):
                # Construct the full path to the source file
                source_file_path = os.path.join(root, file)
                # Copy the file to the destination directory
                shutil.copy2(source_file_path, destination_path)

if __name__ == "__main__":

    root = Tk()
    root.withdraw() # Hide the main tkinter window as we are only using the dialog boxes
    
    # Prompt the user to select a directory as the source path for copying files
    volume_path = filedialog.askdirectory(title="Select volume path...")
    # Ask the user to input the file extension of interest
    files_extension = simpledialog.askstring(title="Info required", prompt="Enter the file extension to look for:")
    # Ask the user to input a prefix for the new folder where files will be copied
    new_folder_prefix = simpledialog.askstring(title="Info required", prompt="Enter the folder prefix:")

    # Proceed only if all required user inputs are provided
    if volume_path and files_extension and new_folder_prefix:
        # Get the path to the user's desktop
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        # Get the current date in 'YYYY-MM-DD' format
        today = datetime.now().strftime('%Y-%m-%d')
        # Create the destination folder name using the provided prefix and current date
        destination_folder_name = "_".join([new_folder_prefix, today])
        # Construct the full path to the destination folder using the newly formed name.
        destination_folder_path = os.path.join(desktop_path, destination_folder_name)
        # Create the destination folder if it doesn't already exist
        os.makedirs(destination_folder_path, exist_ok=True)

        # Execute the file copying operation
        copy_files_with_extension(volume_path, destination_folder_path, files_extension)

        # Inform the user upon successful completion of the file copying
        messagebox.showinfo(title="Success", message="Finished copying")
