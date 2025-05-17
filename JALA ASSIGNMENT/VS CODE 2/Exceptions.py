#Write a program to generate Arithmetic Exception without exception handling
# This will raise a ZeroDivisionError
print("Attempting to divide by zero...")
result = 10 / 1  # Division by zero

print(f"Result: {result}") 

#Handle the Arithmetic exception using try-catch block
# Division with exception handling
a = 5
b = 0

try:
    c = a / b  # This will raise ZeroDivisionError
    print("Result:", c)
except ZeroDivisionError:
    print("Arithmetic Exception caught: Cannot divide by zero.")


#Write a method which throws exception, Call that method in main class without try block
def divide():
    denominator = 2  # Set to non-zero value
    result = 10 / denominator
    print("Result is:", result)

# Calling the method without try-except
print("Calling divide() method...")
divide()

print("This line will be executed.")

#Write a program with multiple catch blocks
def perform_operations():
    a = 10
    b = 0
    arr = [1, 2, 3]

    try:
        print("Trying risky operations...")
        result = a / b  # Will raise ZeroDivisionError
        print("Result:", result)

        print(arr[5])  # Will raise IndexError (not reached due to earlier error)

    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Cannot divide by zero.")

    except IndexError:
        print("Caught IndexError: List index out of range.")

    except Exception as e:
        print("Caught General Exception:", str(e))

# Main section
print("Calling perform_operations()...")
perform_operations()
print("Program continues after exception handling.")


#Write a program to throw exception with your own message
def check_age(age):
    if age < 18:
        raise ValueError("Access denied: Age must be 18 or above.")
    else:
        print("Access granted.")

# Main code
print("Checking age...")
check_age(16)  # This will raise an exception with custom message
print("This line will not be executed if exception occurs.")


#Write a program to create your own exception
# Step 1: Define a custom exception class
class AgeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Step 2: Function that raises the custom exception
def check_age(age):
    if age < 18:
        # Raising the custom exception with a message
        raise AgeException("Age must be 18 or above.")
    else:
        print("Access granted.")

# Main code to call the function
try:
    print("Checking age...")
    check_age(15)  # This will raise the custom AgeException
except AgeException as e:
    print(f"Custom Exception Caught: {e}")


#Write a program with finally block
def divide_numbers(a, b):
    try:
        result = a / b  # May raise ZeroDivisionError
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Execution completed, inside the finally block.")

# Main code
print("Calling divide_numbers() with 10 and 2...")
divide_numbers(10, 2)

print("\nCalling divide_numbers() with 10 and 0...")
divide_numbers(10, 0)

#Write a program to generate Arithmetic Exception
# Function that performs division by zero to generate Arithmetic Exception
def divide_by_zero():
    print("Attempting to divide by zero...")
    result = 10 / 0  # This will raise ZeroDivisionError
    print(f"Result: {result}")

# Main code
divide_by_zero()


#Write a program to generate FileNotFoundException
# Function to open a non-existent file
def open_non_existent_file():
    print("Attempting to open a non-existent file...")
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)

# Main code
open_non_existent_file()

#Write a program to generate ClassNotFoundException
# Function that simulates ClassNotFoundException behavior
def load_class():
    try:
        # Simulate the error manually (instead of actual broken import)
        raise ImportError("Simulated: cannot import name 'NonExistentClass' from 'nonexistent_module'")
    except ImportError as e:
        print(f"ImportError caught: {e}")

# Main code
load_class()


#Write a program to generate IOException
# Function that attempts to read a non-existent file, which can generate an IOError
def generate_io_exception():
    try:
        # Trying to read a file that doesn't exist
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"IOError: {str(e)}")

# Main code
generate_io_exception()

# Write a program to generate NoSuchFieldException
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Function to simulate NoSuchFieldException by accessing a non-existent field
def access_non_existent_field():
    try:
        person = Person("John", 30)
        # Trying to access a non-existent field 'address'
        print(person.address)
    except AttributeError as e:
        print(f"AttributeError: {str(e)}")

# Main code
access_non_existent_field()

