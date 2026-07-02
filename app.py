import os

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File Name {filename}: Generated successfully!")
    except FileExistsError:
        print(F"File name {filename} Already exists!")
    except Exception as E:
        print("An error occurred while creating the file!")
        
def view_files():
    files = os.listdir()
    if not files:
        print("No files found in the current directory!")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)
            
def remove_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been removed successfully!")
    except FileNotFoundError:
        print("File not found!")
    
    except Exception as E:
        print("An error occurred while removing the file!")