#Write a program to print your name 
print("CH.Pavithra")

#Write a program for a Single line comment and multi-line comments

# This is a single-line comment in Python
# This prints a greeting message
print("Hello, World!")  

#Define variables for different Data Types int, Boolean, char, float, double and print on the comsole.

a = 2
print("Type of a: ", type(a))
b = True
print("Type of b: ", type(b))
c = 2.0
print("Type of c: ", type(c))
String = 'RiseON'
print("Type of String: ", type(String))

#Define the local and Global variables with the same name and print both variables and understand the scope of the variables

# Global variable
a = "I am a global variable"

def my_function():
    # Local variable with the same name
    b = "I am a local variable"
    print("Inside function:", b)

my_function()

# Print the global variable
print("Outside function:", a)