import os
import shutil

# Source directory containing both image and XML files
source_directory = './datasets/test'

# Destination directories for images and XML files
images_destination = './datasets/images'
xml_destination = './datasets/annots'

# Ensure the destination directories exist
os.makedirs(images_destination, exist_ok=True)
os.makedirs(xml_destination, exist_ok=True)

# Loop through the files in the source directory
for filename in os.listdir(source_directory):
    source_file = os.path.join(source_directory, filename)

    # Check if the file is an image (you can modify the condition based on your file naming conventions)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # If it's an image, move it to the images destination directory
        destination_file = os.path.join(images_destination, filename)
        shutil.move(source_file, destination_file)
    elif filename.lower().endswith('.xml'):
        # If it's an XML file, move it to the XML destination directory
        destination_file = os.path.join(xml_destination, filename)
        shutil.move(source_file, destination_file)

print("Files have been split into images and XML folders.")
