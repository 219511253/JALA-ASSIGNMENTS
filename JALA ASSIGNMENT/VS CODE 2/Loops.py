#Write a program to print “Bright IT Career” ten times using for loop
for i in range(5):
    print("Bright IT Career")

#Write a java program to print 1 to 20 numbers using the while loop.
# does NOT support switch-case statements
# Initialize a counter variable
i = 1
# Loop from 1 to 20 using while
while i <= 20:
    print(i)
    i += 1  # Increment the counter

#Program to equal operator and not equal operators
#Take two numbers as input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#Check if the numbers are equal using '=='
if a == b:
    print("The numbers are equal (a == b): True")
else:
    print("The numbers are equal (a == b): False")

#Check if the numbers are not equal using '!='
if a != b:
    print("The numbers are not equal (a != b): True")
else:
    print("The numbers are not equal (a != b): False")

#Write a program to print the odd and even numbers.
# Ask the user for the limit
limit = int(input("Enter the range limit: "))

#Use a for loop to go through numbers from 1 to the given limit
print("Even numbers:")
for i in range(1, limit + 1):
    if i % 2 == 0:
        print(i)

print("Odd numbers:")
for i in range(1, limit + 1):
    if i % 2 != 0:
        print(i)

#Write a program to print largest number among three numbers.
#Take three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

#Compare the numbers using if-elif-else statements
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

#Write a program to print even number between 10 and 20 using while
#Initialize the starting number
num = 10

#Use a while loop to check numbers up to 20
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1  

#Write a program to print 1 to 10 using the do-while loop statement.
#Initialize the starting number
i = 1

#Simulate do-while loop using while True
while True:
    print(i)
    i += 1
    if i > 10:
        break  

#Write a program to find Armstrong number or not
# Take input from the user
num = int(input("Enter a number: "))

#Find the number of digits
num_digits = len(str(num))

#Calculate the sum of digits raised to the power of num_digits
sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

#Check if the number is equal to the sum
if num == sum_of_powers:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

#Write a program to find the prime or not
#Take input from the user
num = int(input("Enter a number: "))

#Check if the number is less than or equal to 1
if num <= 1:
    print(num, "is not a prime number.")
else:
    #Check for factors from 2 to sqrt(num)
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

#Write a program to palindrome or not.
#Take input from the user
num = int(input("Enter a number: "))

#Reverse the number
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check if the number is a palindrome
if original == reverse:
    print(original, "is a palindrome number.")
else:
    print(original, "is not a palindrome number.")

# Program to check whether a number is EVEN or ODD using switch
#Take input from the user
num = int(input("Enter a number: "))

#Check even or odd using if-else
if num % 2 == 0:
    print(num, "is EVEN.")
else:
    print(num, "is ODD.")

#Print gender (Male/Female) program according to given M/F using switch
#Take input from the user
gender_input = input("Enter your gender (M/F): ").upper()

#Simulate switch-case using a dictionary
def male():
    print("Gender: Male")

def female():
    print("Gender: Female")

def invalid():
    print("Invalid input. Please enter 'M' or 'F'.")

# Dictionary as a switch substitute
gender_switch = {
    "M": male,
    "F": female
}
gender_switch.get(gender_input, invalid)()



