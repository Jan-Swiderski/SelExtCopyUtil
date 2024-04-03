import os
import shutil
import sys
import platform
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, ttk
import threading

def copy_files_with_extension(source_path: str, destination_path: str, extension: str, callback):
    """
    Copies files with a specified extension from the source to the destination directory.
    Calls a callback function upon completion.
    """
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(extension.upper()) or file.endswith(extension.lower()):
                source_file_path = os.path.join(root, file)
                shutil.copy2(source_file_path, destination_path)
    callback()

def on_copy_complete():
    """
    Displays a success message and destroys the GUI root window upon copy completion.
    """
    messagebox.showinfo(title="Success", message="Finished copying")
    root.destroy()

def run_copy():
    """
    Gathers user inputs from the GUI, creates a destination directory based on these inputs,
    and initiates the file copying process in a new thread.
    """
    source_path = source_path_entry.get()
    destination_path = destination_path_entry.get()
    files_extension = files_extension_entry.get()
    new_folder_prefix = new_folder_prefix_entry.get()
    selected_date_format = date_format_combobox.get().replace('YYYY', '%Y').replace('MM', '%m').replace('DD', '%d')
    if source_path and destination_path and files_extension and new_folder_prefix:
        run_button.config(text="Running...", state="disabled")
        source_path_entry.config(state="disabled")
        source_path_button.config(state="disabled")
        destination_path_entry.config(state="disabled")
        destination_path_button.config(state="disabled")
        files_extension_entry.config(state="disabled")
        new_folder_prefix_entry.config(state="disabled")
        date_format_combobox.config(state="disabled")
        today = datetime.now().strftime(selected_date_format)
        destination_folder_name = "_".join([new_folder_prefix, today])
        destination_folder_path = os.path.join(destination_path, destination_folder_name)
        os.makedirs(destination_folder_path, exist_ok=True)

        thread = threading.Thread(target=copy_files_with_extension, args=(source_path, destination_folder_path, files_extension, on_copy_complete), daemon=True)
        thread.start()
    else:
        messagebox.showwarning(title="Warning", message="Please fill in all fields")

def browse_source():
    """
    Opens a file dialog to select the source directory and updates the source path entry in the GUI.
    """
    directory = filedialog.askdirectory()
    if directory:
        source_path_entry.delete(0, "end")
        source_path_entry.insert(0, directory)

def browse_destination():
    """
    Opens a file dialog to select the destination directory and updates the destination path entry in the GUI.
    """
    directory = filedialog.askdirectory()
    if directory:
        destination_path_entry.delete(0, "end")
        destination_path_entry.insert(0, directory)

if __name__ == "__main__":
    # Initialize the GUI for the SelExtCopyUtil application.
    # This includes setting up the UI components, event handlers, and starting the main event loop.
    root = Tk()
    root.title("SelExtCopyUtil")
    
    if platform.system() == "Windows":
        root.iconbitmap(os.path.join(sys._MEIPASS, 'icons/SelExtCopyUtil_ICON.ico'))
    elif platform.system() == "Darwin":
        root.iconbitmap(os.path.join(sys._MEIPASS, 'icons/SelExtCopyUtil_ICON.icns'))

    root.geometry("600x200")
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)

    Label(root, text="Source Directory:").grid(row=0, column=0, sticky="ew")
    source_path_entry = Entry(root)
    source_path_entry.grid(row=0, column=1, sticky="ew", padx=5)
    source_path_button = Button(root, text="Browse...", command=browse_source)
    source_path_button.grid(row=0, column=2, sticky="ew")

    Label(root, text="Destination Directory:").grid(row=1, column=0, sticky="ew")
    destination_path_entry = Entry(root)
    destination_path_entry.grid(row=1, column=1, sticky="ew", padx=5)
    destination_path_button = Button(root, text="Browse...", command=browse_destination)
    destination_path_button.grid(row=1, column=2, sticky="ew")

    Label(root, text="File Extension:").grid(row=2, column=0, sticky="ew")
    files_extension_entry = Entry(root)
    files_extension_entry.grid(row=2, column=1, sticky="ew", padx=5)

    Label(root, text="Folder Prefix:").grid(row=3, column=0, sticky="ew")
    new_folder_prefix_entry = Entry(root)
    new_folder_prefix_entry.grid(row=3, column=1, sticky="ew", padx=5)

    date_format_label = Label(root, text="Select Date Format:")
    date_format_label.grid(row=5, column=0, sticky="ew")
    date_formats = ['YYYY-MM-DD', 'DD-MM-YYYY', 'MM-DD-YYYY']
    date_format_combobox = ttk.Combobox(root, values=date_formats, state="readonly")
    date_format_combobox.grid(row=5, column=1, sticky="ew", padx=5)
    date_format_combobox.current(1)

    run_button = Button(root, text="Run", command=run_copy)
    run_button.grid(row=6, column=0, columnspan=3, sticky="ew")
    Button(root, text="Exit", command=root.destroy).grid(row=6, column=2, sticky="ew")

    root.mainloop()
