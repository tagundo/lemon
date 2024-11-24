import os
import binascii
import shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the main window

def process_file(file_path):
    with open(file_path, 'rb') as file:
        content = bytearray(file.read())
        # Check for AB 00 Hex at the beginning
        if content[:9] == b'\xAB\x00\x55\x6E\x69\x74\x79\x46\x53':
            # Remove AB 00 Hex from the start
            content = content[2:]
            with open(file_path, 'wb') as modified_file:
                modified_file.write(content)
            return True
    return False

def process_folder(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if process_file(file_path):
                # Move the file to the outside
                shutil.move(file_path, os.path.join(root_folder, filename))

pathtodecrytpt = filedialog.askdirectory(title="Locate Assets Folder")
if pathtodecrytpt:
    print(f"Selected folder: {pathtodecrytpt}")
else:
    print("No folder selected")
    sys.exit(1)
process_folder(pathtodecrytpt)
