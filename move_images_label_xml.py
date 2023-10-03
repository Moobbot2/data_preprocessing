import os
import shutil

def move_images_label_xml(directory_annotations_path, directory_img_path, destination_path):
    """
        Move images associated with XML annotations from one directory to another.

        Parameters:
        - directory_annotations_path (str): The path to the directory containing XML annotation files.
        - directory_img_path (str): The path to the directory containing image files.
        - destination_path (str): The path to the destination folder where image files will be moved.

        Output:
        - None

        This function iterates through XML annotation files in 'directory_annotations_path', extracts
        the base filename, and looks for a corresponding image file in 'directory_img_path'. If found,
        it moves the image file to 'destination_path'. If no corresponding image file is found, it
        prints a message and continues to the next XML file.

        Note: This assumes image files have the same base filename as their corresponding XML files.
        Any non-XML files in 'directory_annotations_path' are skipped.
    """
    for filename in os.listdir(directory_annotations_path):
        if not filename.endswith('.xml'):
            continue  # Skip non-XML files
        
        # Extract the base filename (without the extension)
        base_filename = os.path.splitext(filename)[0]
        
        # Construct the full paths for the XML file and the image file
        xml_filepath = os.path.join(directory_annotations_path, filename)
        image_filepath = ''

        # Find the corresponding image file by looking for files that start with the base filename
        for img_filename in os.listdir(directory_img_path):
            if img_filename.startswith(base_filename):
                image_filepath = os.path.join(directory_img_path, img_filename)
                break
        
        # Check if the image file exists
        if not os.path.isfile(image_filepath):
            print(f"Image file not found for {xml_filepath}. Skipping...")
            continue
        
        # Move the image file to the destination folder
        shutil.move(image_filepath, destination_path)

        print(f"Image file has been moved from {image_filepath} to {destination_path}")

# Example usage:
directory_annotations_path = 'D:\TF\dataset\Annotations\PANO_225'
directory_img_path = 'D:\TF\dataset\JPEGImages'
destination_path = 'D:\TF\dataset\JPEGImages\PANO_225'

move_images_label_xml(directory_annotations_path, directory_img_path, destination_path)
