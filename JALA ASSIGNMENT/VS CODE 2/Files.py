#Write a program to read text file
file_name = input("Enter the name of the file to read: ")
try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        print("\n--- File Contents ---")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#Write a program to write text to .txt file using InputStream
# Ask user for the file name to write to
file_name = input("Enter the name of the file to write to (e.g., output.txt): ")

# Ask user for the content to write
print("Enter the text you want to write to the file (type 'END' on a new line to finish):")

lines = []
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    lines.append(line)

# Write the lines to the file
try:
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print(f"\nText successfully written to '{file_name}'.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

#Write a program to read a file stream
# Ask user for the file name
file_name = input("Enter the file name to read: ")

try:
    # Open the file as a stream
    with open(file_name, 'r') as file:
        print("\n--- File Contents ---")
        for line in file:
            # Print each line without adding extra newline
            print(line, end='')
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Write a program to read a file stream supports random access
# Open a file with random access support
file_name = input("Enter the file name to read: ")

try:
    with open(file_name, 'r') as file:
        print("\n--- File Information ---")
        
        # Print the full contents
        content = file.read()
        print("Full content of the file:")
        print(content)
        
        # Go back to the beginning
        file.seek(0)
        print("\nRe-reading from the beginning:")
        print(file.readline())  # Read the first line

        # Seek to a specific position (e.g., 10th byte)
        position = 10
        file.seek(position)
        print(f"\nReading from byte position {position}:")
        print(file.readline())  # Read from byte 10 to the end of line

        # Show current file pointer position
        current_pos = file.tell()
        print(f"\nCurrent file pointer is at position: {current_pos}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#Write a program to read a file a just to a particular index using seek()
# Prompt the user to enter the file name
file_name = input("Enter the file name to read: ")

# Prompt the user to enter the index to seek to
try:
    index = int(input("Enter the byte index to jump to: "))
except ValueError:
    print("Invalid index. Please enter an integer.")
    exit()

try:
    # Open the file in text mode for reading
    with open(file_name, 'r') as file:
        # Move the file pointer to the given index
        file.seek(index)

        # Read from the index to the end of the file
        content = file.read()

        print(f"\n--- Content from byte index {index} ---")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except OSError as e:
    print(f"Error accessing file: {e}")


#Write a program to check whether a file is having read access and write access permissions
import os

# Ask the user for the file name
file_name = input("Enter the file name to check permissions: ")

# Check if the file exists
if not os.path.exists(file_name):
    print("File does not exist.")
else:
    # Check read access
    can_read = os.access(file_name, os.R_OK)
    
    # Check write access
    can_write = os.access(file_name, os.W_OK)

    print(f"\nPermissions for '{file_name}':")
    print("Readable: Yes" if can_read else "Readable: No")
    print("Writable: Yes" if can_write else "Writable: No")
