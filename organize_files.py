import os
import shutil
import sys

def organize_files_by_extension(directory_path):
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.

    Args:
        directory_path (str): The path to the directory to organize.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.", file=sys.stderr)
        return

    print(f"Starting file organization in: {directory_path}")

    # Iterate through all items in the specified directory
    for filename in os.listdir(directory_path):
        source_path = os.path.join(directory_path, filename)

        # Skip directories and symbolic links to avoid moving them
        if os.path.isdir(source_path) or os.path.islink(source_path):
            continue

        # Get the file extension
        # os.path.splitext returns a tuple: ('filename', '.extension')
        # We take the second element and remove the leading dot.
        file_extension = os.path.splitext(filename)[1].lower().strip('.')

        # If there's no extension (e.g., a file named 'README'), put it in an 'others' folder
        if not file_extension:
            file_extension = "no_extension"

        # Define the target subdirectory for this extension
        destination_subdir = os.path.join(directory_path, file_extension)

        try:
            # Create the subdirectory if it doesn't exist
            os.makedirs(destination_subdir, exist_ok=True)

            # Define the full destination path for the file
            destination_path = os.path.join(destination_subdir, filename)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{file_extension}/'")
        except OSError as e:
            print(f"Error moving '{filename}': {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {e}", file=sys.stderr)

    print(f"File organization complete for: {directory_path}")

if __name__ == "__main__":
    # Check if a directory path was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python organize_files.py <directory_path>")
        print("Example: python organize_files.py /path/to/my/documents")
        # You can set a default directory for testing if no argument is provided
        # For example:
        # target_directory = os.path.expanduser("~/Downloads")
        # organize_files_by_extension(target_directory)
    else:
        target_directory = sys.argv[1]
        organize_files_by_extension(target_directory)
