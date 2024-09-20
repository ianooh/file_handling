# file_handling_assignment.py

def write_to_file():
    try:
        # Create and open file in write mode
        with open('my_file.txt', 'w') as file:
            # Writing three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("The number of students is 25.\n")
            file.write("Good luck with your project!\n")
        print("Writing to file completed.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Write operation ended.")


def read_from_file():
    try:
        # Open file in read mode and display contents
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Contents:")
            print(content)
    except FileNotFoundError:
        print("File not found: Ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Read operation ended.")


def append_to_file():
    try:
        # Open file in append mode and add more lines
        with open('my_file.txt', 'a') as file:
            file.write("This is an appended line.\n")
            file.write("Appending more data: 45.\n")
            file.write("End of file operations.\n")
        print("Appending to file completed.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Append operation ended.")


if __name__ == "__main__":
    write_to_file()  
    read_from_file()  
    append_to_file()  
    read_from_file() 
