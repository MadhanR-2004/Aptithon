import os
import shutil

def rename_images(folder_path, prefix='image'):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (you may need to customize this based on the types of images you have)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Check if there are 40 or more image files
    if len(image_files) < 40:
        print(f"There are not enough images in the folder. There are {len(image_files)} images.")
        return

    # Sort image files to ensure sequential order
    image_files.sort()

    # Iterate through the image files and rename them
    for i, file in enumerate(image_files, start=1):
        # Generate the new filename with the specified prefix and sequential index
        new_filename = f"{prefix}_{i}{os.path.splitext(file)[1]}"
        
        # Create the full paths for the old and new filenames
        old_filepath = os.path.join(folder_path, file)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # Rename the file
        shutil.move(old_filepath, new_filepath)
        print(f"Renamed '{file}' to '{new_filename}'.")

# Example usage: Replace 'your_folder_path' with the path to your folder containing images
rename_images('C:/Users/ragul/Downloads/ap/picsss/pics')
