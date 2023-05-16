import os
import shutil

def organize_files(directory):
    # Specify the existing folders where files should be organized
    folders = {
        '.otf': 'D:\organizefolder',
        '.ttf': 'D:\organizefolder',
        '.jpg': 'D:\organizefolder',
        '.mp3': 'D:\organizefolder',
        '.png': 'D:\organizefolder',
        '.mp4': 'D:\organizefolder',
        '.pdf': 'D:\organizefolder',
        '.svg': 'D:\organizefolder',
        '.wav': 'D:\organizefolder',
        '.jpeg': 'D:\organizefolder',
        # Add more extensions and corresponding folder paths as needed
    }

    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()
            
            if file_extension in folders:
                # Get the destination folder path
                destination_folder = folders[file_extension]
                
                # Move the file to the destination folder
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {destination_folder}")
# Specify the folder to be organized
directory_to_organize = 'C:\\Users\\username\\folder\\'

# Call the function to organize the files
organize_files(directory_to_organize)
