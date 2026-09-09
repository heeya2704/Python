# Write a script that uses the os module to create a new folder named 
# 'MyDownloads' in your current working directory, then print the absolute path of the new folder.

import os

folder_name = "MyDownloads"

os.makedirs(folder_name, exist_ok=True)
absolute_path = os.path.abspath(folder_name)

print(f"Folder '{folder_name}' created successfully.")
print(f"Absolute Path: {absolute_path}")
