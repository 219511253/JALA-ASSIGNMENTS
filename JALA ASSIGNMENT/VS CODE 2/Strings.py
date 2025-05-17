#Different ways creating a string
# 1. Using single quotes
str1 = 'Hello with single quotes'

# 2. Using double quotes
str2 = "Hello with double quotes"

# 3. Using triple single quotes (multi-line)
str3 = '''Hello
with
triple single quotes'''

# 4. Using triple double quotes (multi-line)
str4 = """Hello
with
triple double quotes"""

# 5. Using str() constructor
str5 = str(12345)  # Converts number to string

# 6. Using string concatenation
str6 = "Hello" + " " + "World"

# 7. Using f-strings (formatted string literals)
name = "Alice"
str7 = f"Hello, {name}"

# 8. Using format() method
str8 = "Hello, {}".format(name)

# 9. Creating string from list of characters
chars = ['H', 'e', 'l', 'l', 'o']
str9 = ''.join(chars)

# 10. Using raw string (ignores escape sequences)
str10 = r"C:\Users\Name\Documents"

# Print all strings
print("1:", str1)
print("2:", str2)
print("3:", str3)
print("4:", str4)
print("5:", str5)
print("6:", str6)
print("7:", str7)
print("8:", str8)
print("9:", str9)
print("10:", str10)


#Concatenating two strings using + operators
# Define two strings
str1 = "Hello"
str2 = "World"

# Concatenate using + operator
result = str1 + " " + str2

# Print the result
print("Concatenated String:", result)


#Finding the length of the string
# Define a string
my_string = "RISEON"

# Find the length using len()
length = len(my_string)

# Print the result
print("Length of the string:", length)

#Extract a string using Substring
# Define the original string
text = "Bright IT Career"

# Extract substring from index 0 to 6 (excluding 6)
substring = text[0:6]

# Print the original and the substring
print("Original String:", text)
print("Extracted Substring:", substring)


#Searching in strings using index()
# Define the original string
text = "Bright IT Career"

# Use the index() method to find the position of a substring
position = text.index("IT")

# Print the result
print("The index of 'IT' is:", position)


#Matching a String Against a Regular Expression With matches()
import re

# Define a string
text = "Hello123"

# Using re.match() to check if the string starts with "Hello" followed by digits
match_result = re.match(r"Hello\d+", text)

if match_result:
    print("Match found using re.match():", match_result.group())
else:
    print("No match found using re.match()")

# Using re.fullmatch() to check if the entire string is "Hello" followed by digits
full_match_result = re.fullmatch(r"Hello\d+", text)

if full_match_result:
    print("Full match found using re.fullmatch():", full_match_result.group())
else:
    print("No full match found using re.fullmatch()")


#Comparing strings
# Define two strings
str1 = "apple"
str2 = "banana"

# Function to compare strings manually
def compare_strings(s1, s2):
    # Check if the lengths of both strings are the same
    if len(s1) != len(s2):
        return "Strings are not equal"

    # Compare each character in both strings
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return "Strings are not equal"
    
    return "Strings are equal"

# Compare the strings
result = compare_strings(str1, str2)
print(result)  # Output: Strings are not equal


#startsWith(), endsWith() and compareTo()
# Define two strings
str1 = "Bright IT Career"
str2 = "Bright IT"

# 1. Check if the string starts with a specific word
print(str1.startswith("Bright"))  # True, because str1 starts with "Bright"

# 2. Check if the string ends with a specific word
print(str1.endswith("Career"))  # True, because str1 ends with "Career"

# 3. Compare two strings (lexicographically)
print(str1 > str2)  # True, because "Bright IT Career" is greater than "Bright IT"
print(str1 < str2)  # False, because "Bright IT Career" is not smaller than "Bright IT"
print(str1 == str2) # False, because they are not the same


#Trimming strings with strip()
# Define a string with spaces at the beginning and end
text = "   Hello, Bright IT Career!   "

# Trim the spaces using strip()
trimmed_text = text.strip()

# Print the result
print("Original text:", repr(text))  # Showing the spaces with repr()
print("Trimmed text:", repr(trimmed_text))


#Replacing characters in strings with replace()
# Define a string
text = "Hello, Bright IT Career! Bright IT Career is great!"

# Replace 'Bright IT' with 'Awesome'
new_text = text.replace("Bright IT", "Awesome")

# Print the original and new text
print("Original text:", text)
print("New text:", new_text)


#Splitting strings with split()
# Define a string with spaces
text = "Hello, Bright IT Career is amazing"

# Split the string at each space
words = text.split()

# Print the result
print("Words:", words)


#Converting integer objects to Strings
# Define an integer
num = 123

# 1. Using str() function
str_num = str(num)
print("Using str():", str_num)  # '123'

# 2. Using f-strings (formatted string literals)
f_string_num = f"{num}"
print("Using f-string:", f_string_num)  # '123'

# 3. Using format() method
format_string_num = "{}".format(num)
print("Using format():", format_string_num)  # '123'


#Converting to uppercase and lowercase
# Define a string
text = "Hello, Bright IT Career!"

# Convert to uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)  # "HELLO, BRIGHT IT CAREER!"

# Convert to lowercase
lower_text = text.lower()
print("Lowercase:", lower_text)  # "hello, bright it career!"

