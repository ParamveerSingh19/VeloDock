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
        
def read_file(filename):
    try:
        with open("draft.txt", "r") as f:
            content = f.read()
            print(f"Content of '{filename}': \n{content}")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as E:
        print("An error occurred while reading the file!")
        
def update_file(filename):
    try:
        with open("draft.txt", "a") as f:
            content = input("Enter the content to append to the file: ")
            f.write(content + "\n")
            print("Content appended successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as E:
        print("An error occurred while updating the file!")
        
def main():
    while True:
        print("\nVeloDock")
        print("1. Create a file")
        print("2. View files")
        print("3. Remove a file")
        print("4. Read a file")
        print("5. Update a file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)
        elif choice == "2":
            view_files()
        elif choice == "3":
            filename = input("Enter the filename you want to remove: ")
            remove_file(filename)
        elif choice == "4":
            filename = input("Enter the filename you want to read: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the filename you want to update: ")
            update_file(filename)
        elif choice == "6":
            print("Exiting VeloDock...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
if __name__ == "__main__":
    main()