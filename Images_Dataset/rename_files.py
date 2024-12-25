import os

# Path to the folder containing the files
folder_path = r'C:\Users\Vaibhav\Desktop\Study\AI ML\Sports Celebrity Image Classification\Images_Dataset\usain_bolt'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter only files (not directories)
files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

# Loop through the files and rename them
for index, file in enumerate(files, start=1):
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    
    # New filename format
    new_name = f"usain_bolt_{index}{file_extension}"
    
    # Get the old and new file paths
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)

print("Files renamed successfully.")
