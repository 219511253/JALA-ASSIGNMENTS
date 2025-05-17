#Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(a, b):
    print("Addition (a + b):", a + b)
    print("Subtraction (a - b):", a - b)
    print("Multiplication (a * b):", a * b)
    if b != 0:
        print("Division (a / b):", a / b)
    else:
        print("Division (a / b): Cannot divide by zero")
arithmetic_operations(2,5)

#Write a method for increment and decrement operators(++, --)
def increment_decrement():
    # Declare and initialize a variable
    num = 10
    print("Initial value of num:", num)
    
    # Increment the value by 1
    num = num + 1
    print("After increment (num = num + 1):", num)
    
    # Decrement the value by 1
    num = num - 1  
    print("After decrement (num = num - 1):", num)

# Call the function
increment_decrement()

#Write a program to find the two numbers equal or not.
#Read the first number from the user
num1 = int(input("Enter the first number: "))

# Read the second number from the user
num2 = int(input("Enter the second number: "))

#Compare the two numbers using an if-else statement
if num1 == num2:
    print("The two numbers are equal.")
else:
    print("The two numbers are not equal.")

#Program for relational operators (<,<==, >, >==)
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Use relational operators and display the results
print("a < b  :", a < b)     
print("a <= b :", a <= b)    
print("a > b  :", a > b)     
print("a >= b :", a >= b) 

#Print the smaller and larger number
# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare and find the smaller number
if num1 < num2:
    print("Smaller number is:", num1)
    print("Larger number is:", num2)
elif num1 > num2:
    print("Smaller number is:", num2)
    print("Larger number is:", num1)
else:
    print("Both numbers are equal.")

