import os
import shutil

def check_path(path_to_check, type_path=None):
    """
        Check the existence and type of a file or directory path.

        Parameters:
        - path_to_check (str): The path to be checked.
        - type_path (str, optional): The type of path to check ('dir' for directory, 'file' for file).
                                    If None, only existence is checked.

        Returns:
        - bool: True if the path exists and, if specified, has the correct type. False otherwise.

        This function checks if the specified 'path_to_check' exists. If it exists, it can optionally
        check if the path is of a specific type (file or directory) based on the 'type_path' parameter.

        If 'type_path' is 'dir', it checks if the path is a directory.
        If 'type_path' is 'file', it checks if the path is a file.

        If the path does not exist or does not match the specified type, appropriate error messages
        are printed, and the function returns False. If the path exists and, if specified, is of the
        correct type, the function returns True.
    """
    if not os.path.exists(path_to_check):
        print(f"The path {path_to_check} does not exist.")
        return False

    if type_path == 'dir':
        if not os.path.isdir(path_to_check):
            print(f"The directory at {path_to_check} does not exist.")
            return False

    if type_path == 'file':
        if not os.path.isfile(path_to_check):
            print(f"The file at {path_to_check} does not exist.")
            return False

    return True


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
    if not (os.path.isdir(directory_annotations_path) and
            os.path.isdir(directory_img_path)):
        print(directory_annotations_path,
              os.path.isdir(directory_annotations_path))
        print(directory_img_path, os.path.isdir(directory_img_path))
        return False  # One or more paths are not valid directories
    if not os.path.isdir(destination_path):
        os.makedirs(destination_path)

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
            # shutil.move(xml_filepath, destination_path) #label_not_image
            continue

        # Move the image file to the destination folder
        # shutil.move(image_filepath, destination_path)
        print(f"Image file has been moved from {image_filepath} to {destination_path}")

# Example usage:
directory_annotations_path = r'foder label image xml'
directory_img_path = r'foder image'
destination_path = r'new foder image'

move_images_label_xml(directory_annotations_path, directory_img_path, destination_path)
