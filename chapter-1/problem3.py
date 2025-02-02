import os

def print_directory_contents(path):
    """
    Prints the contents of the specified directory.
    
    :param path: The path of the directory to list.
    """
    try:
        # Check if the path exists and is a directory
        if os.path.exists(path) and os.path.isdir(path):
            print(f"Contents of directory '{path}':")
            # List all files and directories in the specified path
            for item in os.listdir(path):
                print(item)
        else:
            print(f"The path '{path}' does not exist or is not a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = input("Enter the directory path: ")
print_directory_contents(directory_path)