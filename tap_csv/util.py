import os
import shutil

def move_file_to_folder(file_path, target_folder):
    """Move a file to the specified folder, creating the folder if it doesn't exist."""
    
    # Extract the filename from the file_path
    file_name = os.path.basename(file_path)
    
    # Construct the target file path
    directory_path = os.path.join(os.path.dirname(file_path),target_folder)

    # Check if the target folder exists, create it if it does not
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    target_path = os.path.join(directory_path, file_name)
    
    # Move the file
    shutil.move(file_path, target_path)